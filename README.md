  - [NAME](#NAME)
  - [SYNOPSIS](#SYNOPSIS)
  - [DESCRIPTION](#DESCRIPTION)
  - [INTERFACE](#INTERFACE)
      - [plan](#plan)
      - [ok](#ok)
      - [done\_testing](#done_testing)
      - [diag](#diag)
  - [RUNNING THE TESTS](#RUNNING-THE-TESTS)

# NAME

testsimple - Python testing framework inspired by Perl's Test::Simple

# SYNOPSIS

``` 
  from testsimple import *

  plan(tests=1)

  ok(42 > 10, "Math still works")
```

# DESCRIPTION

This module tries to replicate the Test::Simple API. It produces output
in the TAP protocol.

# INTERFACE

## plan

Declares the plan for the tests. While setting the number of tests
manually might seem cumbersome, it comes in handy when the test gets in
an inconsistent state and passes too more or less tests than intended.

``` 
  plan(tests=2)

  ok(True)
  ok(True)
```

## ok

**ok** is the main function of this module. It works as an assertion.

``` 
  ok(10 > 1)
  ok("Test")
  ok(not None, "This should pass")

  ok(False, "This should fail")
```

## done\_testing

**done\_testing** can be placed at the bottom of your test script. The
testsimple module keeps track of the tests you run, so it can generate
the plan for you automatically. This is useful if you're lazy or if your
test is very dynamic.

``` 
  import random
  from testsimple import *

  for _ in range(random.randint(1, 20)):
    ok(True)

  done_testing()
```

## diag

Produces a diagnostic output. This is usually hidden during test runs,
but the test harness can optionally show it to the user. This
information can be useful if the tests are failing and you want to get
details.

``` 
  diag("Testing fetch_user with", username)
```

# RUNNING THE TESTS

You can run the tests using any TAP-compatible test harness. An easy one
to use is *Prove*. All you need to do is put each test script in a
folder called *t*. After that, if you run the *prove* command in the
root directory of the project, it will run each test and print the
results. You can pass flags and configure the behaviour, such as running
tests in parallel or printing diagnostic output.
