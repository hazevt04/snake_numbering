#!/usr/bin/env python3

import math
import time


def debug_func(debug, func, *args):
    if(debug):
        func(*args)


# Script for sliding_window
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()        
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print("{}(): {} ms".format(method.__name__, (te-ts)*1000))
            #%r  %2.2f ms' % \
            #      (method.__name__, (te - ts) * 1000)
        return result
    return timed


def benchmark(num_runs, func, *args):
    milliseconds = 0
    for _ in range(num_runs):
        start_time = time.time()
        result = func(*args)
        milliseconds += time.time() - start_time
    return (milliseconds/num_runs), result


# Script for myutils
def myswap(arr, idx0, idx1, debug=False, prefix_str=''):
    if arr[idx0] != arr[idx1]:
        arr[idx0] ^= arr[idx1]
        arr[idx1] ^= arr[idx0]
        arr[idx0] ^= arr[idx1]


def add_parity(val, debug=False):
    val_bin = bin(val)[2:].rjust(56,'0')
    if debug:
        print("val is {}".format(val))
        print("val_bin is {}".format(val_bin))

    val_pad = ''
    for b in range(0,56,7):
        val_slice = val_bin[b:b+7]
        val_pad += val_slice
        if debug:
            print( "b is {}. b + 7 is {}. val_slice is {}".format(b, b+7, val_slice))
        if val_slice.count('1') & 1:
            val_pad += '0'
        else:
            val_pad += '1'

        if debug:
            print( "b is {}. val_pad is {}".format(b, val_pad))
    
    return int(val_pad,2)
        
def mylog2(val):
    # Pre calc 1/log10(2)
    log10_2 = math.log10(2)
    log10_2_recip = 1/log10_2
    return math.log10(val) * log10_2_recip

if __name__ == '__main__':
    debug = False

    #test_list = [23,33,91]
    #print("Original list is {}".format(test_list))
    #idx0 = 1
    #idx1 = 2
    #myswap(test_list, idx0, idx1, debug )
    #print("list after swapping index {} and index {} is {}".format(idx0, idx1,test_list))

    val56 = 0
    val64 = add_parity( val56, debug )
    # THE 0x counts in the field width specifier in the format specifier below
    # expected field width specifier for 56 bit hex value is :014x, but actually its :016x?!
    print("val56 is {:#016x}".format(val56))
    # expected field width specifier for 64 bit hex value is :016x, but actually its :018x?!
    print("val64 is {:#018x}\n".format(val64))

    val2pow = 1
    for val in range(12):
        val2pow <<= 1
        print("log2({}) = {}".format(val2pow, mylog2(val2pow)))

    notpow2 = 45
    print("log2({}) = {}".format(notpow2, mylog2(notpow2)))
    print()


   


