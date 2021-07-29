/*
 * Copyright (c) 2020 Huawei Technologies Co.,Ltd.
 *
 * openGauss is licensed under Mulan PSL v2.
 * You can use this software according to the terms and conditions of the Mulan PSL v2.
 * You may obtain a copy of Mulan PSL v2 at:
 *
 *          http://license.coscl.org.cn/MulanPSL2
 *
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
 * EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
 * MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
 * See the Mulan PSL v2 for more details.
 */
 
 

"""
copyright (c) 2020 Huawei Technologies Co.,Ltd.

openGauss is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2.
You may obtain a copy of Mulan PSL v2 at:

         http://license.coscl.org.cn/MulanPSL2

THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PSL v2 for more details.
"""
import unittest

from detector.timeseries_algorithms import fb_prophet

timeseries = [(1606189212, 66.0), (1606189213, 55.0), (1606189214, 47.0), (1606189215, 13.0), (1606189216, 107.0),
              (1606189217, 46.0), (1606189218, 39.0), (1606189219, 10.0), (1606189220, 53.0), (1606189221, 54.0),
              (1606189222, 13.0), (1606189223, 50.0), (1606189224, 109.0), (1606189225, 49.0), (1606189226, 46.0),
              (1606189227, 29.0), (1606189228, 97.0), (1606189229, 9.0), (1606189230, 99.0), (1606189231, 26.0),
              (1606189232, 49.0), (1606189233, 12.0), (1606189234, 111.0), (1606189235, 1.0), (1606189236, 63.0),
              (1606189237, 39.0), (1606189238, 114.0), (1606189239, 10.0), (1606189240, 0.0), (1606189241, 43.0),
              (1606189242, 25.0), (1606189243, 91.0), (1606189244, 92.0), (1606189245, 28.0), (1606189246, 87.0),
              (1606189247, 38.0), (1606189248, 43.0), (1606189249, 19.0), (1606189250, 26.0), (1606189251, 118.0),
              (1606189252, 85.0), (1606189253, 66.0), (1606189254, 98.0), (1606189255, 88.0), (1606189256, 53.0),
              (1606189257, 11.0), (1606189258, 112.0), (1606189259, 34.0), (1606189260, 14.0), (1606189261, 93.0),
              (1606189262, 97.0), (1606189263, 114.0), (1606189264, 103.0), (1606189265, 1.0), (1606189266, 71.0),
              (1606189267, 48.0), (1606189268, 19.0), (1606189269, 24.0), (1606189270, 62.0), (1606189272, 28.0),
              (1606189273, 107.0), (1606189274, 67.0), (1606189275, 80.0), (1606189276, 62.0), (1606189277, 40.0),
              (1606189278, 88.0), (1606189279, 76.0), (1606189280, 13.0), (1606189281, 112.0), (1606189282, 55.0),
              (1606189283, 43.0), (1606189284, 38.0), (1606189285, 91.0), (1606189286, 67.0), (1606189287, 46.0),
              (1606189288, 91.0), (1606189289, 88.0), (1606189290, 44.0), (1606189291, 97.0), (1606189292, 71.0),
              (1606189293, 102.0), (1606189294, 90.0), (1606189295, 43.0), (1606189296, 73.0), (1606189297, 92.0),
              (1606189298, 30.0), (1606189299, 6.0), (1606189300, 91.0), (1606189301, 19.0), (1606189302, 94.0),
              (1606189303, 116.0), (1606189304, 15.0), (1606189305, 77.0), (1606189306, 72.0), (1606189307, 102.0),
              (1606189308, 31.0), (1606189309, 81.0), (1606189310, 8.0), (1606189311, 101.0), (1606189312, 84.0)]


class TestProphet(unittest.TestCase):
    def test_prophet(self):
        forecast_model = fb_prophet.FacebookProphet()
        forecast_model.fit(timeseries)
        forecast_result = forecast_model.forecast(forecast_periods='10S')
        self.assertGreater(len(forecast_result), 0)


if __name__ == '__main__':
    unittest.main()
