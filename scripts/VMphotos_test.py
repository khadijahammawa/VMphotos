import os
import unittest

import cropalign
import numpy as np
import pytest
import win32com.client


class PhotoshopTest:
    # This test will check if the remove-bg.jsx file was opened successfully 
    # by checking the number of open documents in the Photoshop application. 
    # If the assert statement passes, the test will be considered successful.
    def test_runPS(self):
        psApp = win32com.client.Dispatch('Photoshop.Application')
        psApp.Open("C:/Users/Khadija_Hammawa/Documents/GitHub/VMphotos/scripts/remove-bg.jsx")
        # Check if the script correctly opened the remove-bg.jsx file
        assert psApp.Documents.Count == 1
        psApp.Quit()

class TestCropAlign(unittest.TestCase): 
    # This test case uses the unittest module to test the two main functions of cropalign.py: 
    # calculate_pupil_offset and crop_and_align. The TestCropAlign class inherits from unittest.
    # TestCase and contains two tests: test_calculate_pupil_offset and test_crop_and_align. 
    # Each test asserts that the expected output is equal to the actual output, using the assertEqual method. 
    # The test will fail if the actual output does not match the expected output.
    def test_calculate_pupil_offset(self):
        # Test data
        imginfo = [{"name": "1", "lx": 10, "ly": 20, "rx": 30, "ry": 40},
                   {"name": "2", "lx": 15, "ly": 25, "rx": 35, "ry": 45}]
        imgdata = [{"name": "1", "use": np.zeros((100, 100, 3))},
                   {"name": "2", "use": np.zeros((100, 100, 3))}]
        # Test calculation of pupil offset
        offset = cropalign.calculate_pupil_offset(imginfo, imgdata)
        self.assertEqual(offset, [(10, 20), (15, 25)])

    def test_crop_and_align(self):
        # Test data
        imginfo = [{"name": "1", "lx": 10, "ly": 20, "rx": 30, "ry": 40, "xdist": 20, "ydist": 20},
                   {"name": "2", "lx": 15, "ly": 25, "rx": 35, "ry": 45, "xdist": 20, "ydist": 20}]
        imgdata = [{"name": "1", "use": np.zeros((100, 100, 3))},
                   {"name": "2", "use": np.zeros((100, 100, 3))}]
        # Test cropping and aligning the images
        aligned_imgs = cropalign.crop_and_align(imginfo, imgdata)
        self.assertEqual(len(aligned_imgs), 2)
        self.assertEqual(aligned_imgs[0].shape, (40, 40, 3))
        self.assertEqual(aligned_imgs[1].shape, (40, 40, 3))

if __name__ == '__main__':
    unittest.main()



        

