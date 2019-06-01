# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
=head1 NAME

testsimple - Python testing framework inspired by Perl's Test::Simple

=head1 SYNOPSIS

  from testsimple import *

  plan(tests=1)

  ok(42 > 10, "Math still works")

=head1 DESCRIPTION

This module tries to replicate the Test::Simple API. It produces output in the
TAP protocol.

=head1 INTERFACE

=cut

"""

"""
=head2 plan

Declares the plan for the tests. While setting the number of tests manually
might seem cumbersome, it comes in handy when the test gets in an inconsistent
state and passes too more or less tests than intended.

  plan(tests=2)

  ok(True)
  ok(True)

=cut

"""
def plan(tests=0):
    print(f"1..{tests}")


__testsimple_test_num = 0

"""
=head2 ok

B<ok> is the main function of this module. It works as an assertion.

  ok(10 > 1)
  ok("Test")
  ok(not None, "This should pass")

  ok(False, "This should fail")

=cut

"""
def ok(condition, msg=""):
    global __testsimple_test_num
    __testsimple_test_num += 1
    prefix = "not ok"

    if condition:
        prefix = "ok"

    print(f"{prefix} {__testsimple_test_num} - {msg}")

"""
=head2 done_testing

B<done_testing> can be placed at the bottom of your test script. The testsimple
module keeps track of the tests you run, so it can generate the plan for you
automatically. This is useful if you're lazy or if your test is very dynamic.

  import random
  from testsimple import *

  for _ in range(random.randint(1, 20)):
    ok(True)

  done_testing()

=cut

"""
def done_testing():
    print(f"1..{__testsimple_test_num}")


"""
=head2 diag

Produces a diagnostic output. This is usually hidden during test runs, but the
test harness can optionally show it to the user. This information can be useful
if the tests are failing and you want to get details.

  diag("Testing fetch_user with", username)

=cut

"""
def diag(*args):
    print("#", *args)

"""
=head1 RUNNING THE TESTS

You can run the tests using any TAP-compatible test harness. An easy one to use
is I<Prove>. All you need to do is put each test script in a folder called
I<t>. After that, if you run the I<prove> command in the root directory of the
project, it will run each test and print the results. You can pass flags and
configure the behaviour, such as running tests in parallel or printing
diagnostic output.

=cut

"""
