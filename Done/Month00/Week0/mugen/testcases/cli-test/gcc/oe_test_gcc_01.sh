#!/usr/bin/bash

source ${OET_PATH}/libs/locallibs/common_lib.sh

function pre_test() {
    LOG_INFO "Start to prepare the test environment."
    DNF_INSTALL gcc
    LOG_INFO "End to prepare the test environment."
}

function run_test() {
    LOG_INFO "Start to run test."

    gcc -v 2>&1 | grep -Pz "gcc version $(rpm -q gcc --queryformat '%{version}') \(GCC\)"
    CHECK_RESULT $? 0 0 "Check gcc -v failed"
    gcc --help | grep -Pz "Usage: gcc \[options\] file..."
    CHECK_RESULT $? 0 0 "Check gcc --help failed"

    LOG_INFO "End to run test."
}

function post_test() {
    LOG_INFO "Start to restore the test environment."
    DNF_REMOVE
    LOG_INFO "End to restore the test environment."
}

main $@
