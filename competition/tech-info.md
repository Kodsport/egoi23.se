---
title: Technical Information
layout: default
background: bkg/max4-2.jpg
---

## Contest Environment

The contest will be run on a VirtualBox virtual machine running Debian 11 and the GNOME desktop environment (version 3.38.5).<br>
An initial version of the contest image can be downloaded [here](https://lfs.schmidb.ch/egoi/CGTa46wwOMn9cp47Djp7gQ/egoi23-vm-20230423.ova).

Preliminarily, the following software will be available (some versions may change to a later version):

<div class="columns-outer">
	<div class="columns-inner">
		<h3>Text Editors</h3>
		<ul>
			<li>Atom 1.60.0</li>
			<li>Code::Blocks 20.03</li>
			<li>Eclipse 2022-11</li>
			<li>Emacs 27.1</li>
			<li>Geany 1.37.1</li>
			<li>Gedit 3.38.1</li>
			<li>Gvim 8.2</li>
			<li>Joe 4.6</li>
			<li>Kate 20.12.2</li>
			<li>KDevelop 5.6.2</li>
			<li>Nano 5.4</li>
			<li>Sublime Text 4143</li>
			<li>Visual Studio Code 1.75.1<br><em>(with C/C++ extension)</em></li>
			<li>PyCharm</li>
		</ul>
	</div>
	<div class="columns-inner">
		<h3>Compilers & Interpreters</h3>
		<ul>
			<li>GCC 10.2.1-6</li>
			<li>PyPy 3.7.10</li>
			<li>Python 3.9.2</li>
			<li>Ruby 2.7 <span class="fl">(not a submission language)</span></li>
		</ul>

		<h3>Debuggers</h3>
		<ul>
			<li>gdb 10.1.90</li>
			<li>valgrind 3.16.1</li>
			<li>DDD 3.3.12</li>
		</ul>

		<h3>Other Software</h3>
		<ul>
			<li>Firefox 102.8.0</li>
			<li>Gnome Terminal 3.38.3</li>
			<li>XTerm 366</li>
		</ul>
	</div>
</div>

Documentation for <a href="https://en.cppreference.com" target="_blank">C++</a> and <a href="https://docs.python.org/3.8/" target="_blank">Python</a> will be available in the contest system.

<div class="hr"></div>

## Judge System
The competition will use the Kattis online judge. The only supported submission languages are C++ and Python. See the <a href="https://open.kattis.com/help" target="_blank">Kattis help page</a> for more information about versions and compilation flags. Note that Kattis uses the PyPy runtime for python, and that the judge system uses GCC version 11.3 whereas the contest image has GCC version 10.

<div class="hr"></div>

## Hardware

Participants competing on-site will use desktop computers at Lund University.

The provided keyboards have Swedish layout, and are of two different models (see the pictures).<br>
Contestants will be able to bring their own wired keyboard and mouse with a USB-A connector (subject to the contest rules).
It is also possible to change the keyboard layout from inside the contest VM.

<img src="/assets/images/keyboard1.jpg" style="max-width: 100%;">
<img src="/assets/images/keyboard2.jpg" style="max-width: 100%;">

<div class="hr"></div>

## Screen Recording

Screen recording is available in the contest VM and can be started by running `egoi recording start` from a terminal.
You can then run `egoi recording status` to verify that screen recording has started successfully, and `egoi recording stop` to stop and upload the recording.

Note that screen recording does not start automatically so teams participating remotely will need to run these commands manually before and after the contest. Screen recording will not be used for participants competing on-site.
