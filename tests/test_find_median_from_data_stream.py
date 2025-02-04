"""
295. Find Median from Data Stream

https://leetcode.com/problems/find-median-from-data-stream
"""

from unittest import TestCase

from src.find_median_from_data_stream import MedianFinder


class TestMedianFinder(TestCase):
    def test_1(self):
        mf = MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        assert mf.findMedian() == 1.5
        mf.addNum(3)
        assert mf.findMedian() == 2.0

    def test_2(self):
        mf = MedianFinder()
        mf.addNum(6)
        assert mf.findMedian() == 6.0
        mf.addNum(10)
        assert mf.findMedian() == 8.0
        mf.addNum(2)
        assert mf.findMedian() == 6.0
        mf.addNum(6)
        assert mf.findMedian() == 6.0
        mf.addNum(5)
        assert mf.findMedian() == 6.0
        mf.addNum(0)
        assert mf.findMedian() == 5.5
        mf.addNum(6)
        assert mf.findMedian() == 6.0
        mf.addNum(3)
        assert mf.findMedian() == 5.5
        mf.addNum(1)
        assert mf.findMedian() == 5.0
        mf.addNum(0)
        assert mf.findMedian() == 4.0
        mf.addNum(0)
        assert mf.findMedian() == 3.0
        mf = MedianFinder()
