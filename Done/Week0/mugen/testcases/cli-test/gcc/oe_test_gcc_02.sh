#!/usr/bin/bash

source ${OET_PATH}/libs/locallibs/common_lib.sh

function pre_test() {
    LOG_INFO "Start to prepare the test environment."
    DNF_INSTALL gcc
    LOG_INFO "End to prepare the test environment."

    cat > test.c <<EOF
#include <stdio.h>

int main(int argc, int *argv[])
{
	printf("hello, world");

	return 0;
}
EOF

}

function run_test() {
    LOG_INFO "Start to run test."

    gcc -S test.c -o test.S
    CHECK_RESULT $? 0 0 "Check gcc -S failed" 1
    gcc test.S -o test.o
    CHECK_RESULT $? 0 0 "Check gcc compile failed" 1
    ./test.o |grep -Pz '^hello, world$'
    CHECK_RESULT $? 0 0 "Check gcc output executable file failed"

    LOG_INFO "End to run test."
}

function post_test() {
    LOG_INFO "Start to restore the test environment."
    DNF_REMOVE
    rm -f test.c test.S test.o
    LOG_INFO "End to restore the test environment."
}

main $@
