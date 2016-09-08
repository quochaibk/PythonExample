'''
Created on Sep 8, 2016

@author: HaiNguyen
'''
import logging

def test_log():
    logging.getLogger(__name__).debug("test log log")
    
if __name__== '__main__':
    test_log()