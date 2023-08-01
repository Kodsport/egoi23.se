#!/usr/bin/env python3

"""
Example usage (with T=1000, N=10):

For python programs, say "solution.py" (normally run as "pypy3 solution.py"):

    python3 testing_tool.py pypy3 solution.py <<<"1000 10"

For C++ programs, first compile it
(e.g. with "g++ -std=gnu++17 solution.cpp -o solution.out")
and then run

    python3 testing_tool.py ./solution.out <<<"1000 10"

"""

from fcntl import fcntl
import os
import random
import signal
import sys
from typing import List, Tuple

F_SETPIPE_SZ = 1031


def error(msg: str) -> None:
    print("ERROR:", msg, file=sys.stderr)
    sys.exit(1)

def parse_int(s: str, what: str, lo: int, hi: int) -> int:
    try:
        ret = int(s)
    except Exception:
        error(f"Failed to parse {what} as integer: {s}")
    if not (lo <= ret <= hi):
        error(f"{what} out of bounds: {ret} not in [{lo}, {hi}]")
    return ret

def wait_for_child(pid: int) -> None:
    pid, status = os.waitpid(pid, 0)
    if os.WIFSIGNALED(status):
        sig = os.WTERMSIG(status)
        error(f"Program terminated with signal {sig} ({signal.Signals(sig).name})")
    ex = os.WEXITSTATUS(status)
    if ex != 0:
        error(f"Program terminated with exit code {ex}")

def read_line(pid: int, file, what: str) -> str:
    line = file.readline()
    if not line:
        wait_for_child(pid)
        error(f"Failed to read {what}: no more output")
    return line.rstrip("\r\n")

def write_line(file, line: str) -> None:
    try:
        file.write(line + "\n")
        file.flush()
    except BrokenPipeError:
        pass

def run_solution(submission: List[str], T: int, N: int, silent: bool) -> int:

    c2p_read, c2p_write = os.pipe()
    p2c_read, p2c_write = os.pipe()
    try:
        fcntl(p2c_read, F_SETPIPE_SZ, 1024 * 1024)
    except Exception:
        print("Warning: failed to increase pipe capacity. Are you using the EGOI VM?")
    pid = os.fork()

    if pid == 0:
        os.close(p2c_write)
        os.close(c2p_read)

        os.dup2(p2c_read, 0)
        os.dup2(c2p_write, 1)

        try:
            os.execvp(submission[0], submission)
        except Exception as e:
            error(f"Failed to execute program: {e}")
        assert False, "unreachable"
    else:
        os.close(c2p_write)
        os.close(p2c_read)

        with os.fdopen(p2c_write, "w") as fout:
            with os.fdopen(c2p_read, "r") as fin:

                tot_queries = 0
                write_line(fout, f"{T} {N}")
                for tc in range(T):
                    perm = list(range(1, N+1))
                    random.shuffle(perm)
                    prefix_sum = [0] * (N+1)
                    for i in range(N):
                        prefix_sum[i+1] = prefix_sum[i] + perm[i]
                    queries = 0
                    target_ind = perm.index(1)
                    if not silent:
                        perm_str = ", ".join(map(str, perm[:4]))
                        if len(perm) > 4:
                            perm_str += ", ..."
                        print(f"[*] Starting round {tc+1}, with permutation {perm_str} and target at position {target_ind}")
                    while True:
                        line = read_line(pid, fin, f"query {queries+1} of round {tc+1}")
                        tokens = line.split()
                        first_tok = tokens[0] if tokens else ''
                        if first_tok == '!':
                            if len(tokens) != 2:
                                error(f"Expected answer in format \"! i\"; got \"{line}\"")
                            if not silent:
                                print(f"[*] Guess: \"{line}\"")

                            guess = parse_int(tokens[1], "guess", 0, N-1)

                            if guess != target_ind:
                                perm_str = " ".join(map(str, perm))
                                # print(f"The permutation was:\n{perm_str}")
                                error(f"Incorrect guess in round {tc+1}: claimed {guess}, but was {target_ind}")
                            break

                        elif first_tok == '?':
                            queries += 1
                            if len(tokens) != 3:
                                error(f"Expected query in format \"? a b\"; got \"{line}\"")

                            if not silent:
                                print(f"[*] Query #{queries}: \"{line}\"")

                            a = parse_int(tokens[1], "left endpoint", 0, N-1)
                            b = parse_int(tokens[2], "right endpoint", 0, N-1)
                            if a > b:
                                error(f"Left endpoint ({a}) is greater than right endpoint ({b})")

                            su = prefix_sum[b+1] - prefix_sum[a]
                            if not silent:
                                print(f"[*] -> {su}")

                            write_line(fout, f"{su}")

                        else:
                            error(f"Expected \"!\" or \"?\", got \"{line}\"")
                    if not silent:
                        print(f"[*] Finished round {tc+1} using {queries} queries")
                    tot_queries += queries

                # Wait for program to terminate, and read all its output
                remainder = fin.read()
                if remainder.strip():
                    error(f"Unexpected trailing output: {remainder}")
                wait_for_child(pid)


    return tot_queries


def main() -> None:
    silent = False
    args = sys.argv[1:]
    if args and args[0] == "--silent":
        args = args[1:]
        silent = True
    if not args:
        print("Usage:", sys.argv[0], '[--silent] program... <<<"T N"')
        sys.exit(0)

    toks = []
    for line in sys.stdin:
        for tok in line.split():
            toks.append(int(tok))
        if len(toks) >= 3:
            break

    if len(toks) != 2:
        error("Need exactly 2 input parameters: T N")
    T, N = toks
    if T < 1:
        error(f"T must be at least one")
    if N < 1:
        error(f"N must be at least one")

    if not silent:
        print(f"[*] Running solution (T = {T}, N = {N})")

    queries = run_solution(args, T, N, silent)
    avg = queries / T

    avg_text = f" (average: {avg:.1f})" if T != 1 else ""
    print(f"[*] OK: total {queries} queries{avg_text}")

if __name__ == "__main__":
    main()

