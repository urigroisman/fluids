# -*- coding: utf-8 -*-
'''Chemical Engineering Design Library (ChEDL). Utilities for process modeling.
Copyright (C) 2018 Caleb Bell <Caleb.Andrew.Bell@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

from fluids import *
import numpy as np
from scipy.constants import inch
from numpy.testing import assert_allclose
import pytest

def test_orifice_discharge():
    m = orifice_discharge(D=0.0739, Do=0.0222, P1=1E5, P2=9.9E4, rho=1.1646, C=0.5988, expansibility=0.9975)
    assert_allclose(m, 0.01120390943807026)
    
def test_orifice_expansibility():
    epsilon = orifice_expansibility(D=0.0739, Do=0.0222, P1=1E5, P2=9.9E4, k=1.4)
    assert_allclose(epsilon, 0.9974739057343425)
    # Tested against a value in the standard
    
def test_orifice_expansivity_1989():
    # No actual sample points
    epsilon = orifice_expansivity_1989(D=0.0739, Do=0.0222, P1=1E5, P2=9.9E4, k=1.4)
    assert_allclose(epsilon, 0.9970510687411718)
    
def test_C_Reader_Harris_Gallagher():
    C = C_Reader_Harris_Gallagher(D=0.07391, Do=0.0222, rho=1.1645909036, mu=0.0000185861753095, m=0.124431876, taps='corner' )
    assert_allclose(C, 0.6000085121444034)
    
    C = C_Reader_Harris_Gallagher(D=0.07391, Do=0.0222, rho=1.1645909036, mu=0.0000185861753095, m=0.124431876, taps='D' )
    assert_allclose(C, 0.5988219225153976)
    
    C = C_Reader_Harris_Gallagher(D=0.07391, Do=0.0222, rho=1.1645909036, mu=0.0000185861753095, m=0.124431876, taps='flange' )
    assert_allclose(C, 0.5990042535666878)

def test_Reader_Harris_Gallagher_discharge():
    m = Reader_Harris_Gallagher_discharge(D=0.07366, Do=0.05, P1=200000.0, P2=183000.0, rho=999.1, mu=0.0011, k=1.33, taps='D')
    assert_allclose(m, 7.702338035732167)
    
    
def test_K_to_discharge_coefficient():
    C = K_to_discharge_coefficient(D=0.07366, Do=0.05, K=5.2314291729754)
    assert_allclose(C, 0.6151200000000001)
    
def test_discharge_coefficient_to_K():
    K = discharge_coefficient_to_K(D=0.07366, Do=0.05, C=0.61512)
    assert_allclose(K, 5.2314291729754)
    
def test_dP_orifice():
    dP = dP_orifice(D=0.07366, Do=0.05, P1=200000.0, P2=183000.0, C=0.61512)
    assert_allclose(dP, 9069.474705745388)
    
def test_velocity_of_approach_factor():
    factor = velocity_of_approach_factor(D=0.0739, Do=0.0222)
    assert_allclose(factor, 1.0040970074165514)

def test_orifice_flow_coefficient():
    factor = orifice_flow_coefficient(D=0.0739, Do=0.0222, C=0.6)
    assert_allclose(factor, 0.6024582044499308)
    
def test_nozzle_expansibility():
    epsilon = nozzle_expansibility(D=0.0739, Do=0.0222, P1=1E5, P2=9.9E4, k=1.4)
    assert_allclose(epsilon, 0.991617725452954)

def test_C_long_radius_nozzle():
    C = C_long_radius_nozzle(D=0.07391, Do=0.0422, rho=1.2, mu=1.8E-5, m=0.1)
    assert_allclose(C, 0.9805503704679863)
    
def test_C_ISA_1932_nozzle():
    C = C_ISA_1932_nozzle(D=0.07391, Do=0.0422, rho=1.2, mu=1.8E-5, m=0.1)
    assert_allclose(C, 0.9635849973250495)
    
def test_C_venturi_nozzle():
    C = C_venturi_nozzle(D=0.07391, Do=0.0422)
    assert_allclose(C, 0.9698996454169576)
    
    
def test_diameter_ratio_cone_meter():
    beta = diameter_ratio_cone_meter(D=0.2575, Dc=0.184)
    assert_allclose(beta, 0.6995709873957624)
    # Example in 1 matches exactly; 
    beta = diameter_ratio_cone_meter(D=10.137*inch, Dc=7.244*inch)
    assert_allclose(beta, 0.6995232442563669)


def test_C_ISA_1932_nozzle_full():
    Cs = [[0.9616, 0.9692, 0.9750, 0.9773, 0.9789, 0.9813, 0.9820, 0.9821, 0.9822],
    [0.9604, 0.9682, 0.9741, 0.9764, 0.9781, 0.9805, 0.9812, 0.9813, 0.9814],
    [0.9592, 0.9672, 0.9731, 0.9755, 0.9773, 0.9797, 0.9804, 0.9805, 0.9806],
    [0.9579, 0.9661, 0.9722, 0.9746, 0.9763, 0.9788, 0.9795, 0.9797, 0.9797],
    [0.9567, 0.9650, 0.9711, 0.9736, 0.9754, 0.9779, 0.9786, 0.9787, 0.9788],
    [0.9554, 0.9638, 0.9700, 0.9726, 0.9743, 0.9769, 0.9776, 0.9777, 0.9778],
    [0.9542, 0.9626, 0.9689, 0.9715, 0.9733, 0.9758, 0.9766, 0.9767, 0.9768],
    [0.9529, 0.9614, 0.9678, 0.9703, 0.9721, 0.9747, 0.9754, 0.9756, 0.9757],
    [0.9516, 0.9602, 0.9665, 0.9691, 0.9709, 0.9735, 0.9743, 0.9744, 0.9745],
    [0.9503, 0.9589, 0.9653, 0.9678, 0.9696, 0.9722, 0.9730, 0.9731, 0.9732],
    [0.9490, 0.9576, 0.9639, 0.9665, 0.9683, 0.9709, 0.9717, 0.9718, 0.9719],
    [0.9477, 0.9562, 0.9626, 0.9651, 0.9669, 0.9695, 0.9702, 0.9704, 0.9705],
    [0.9464, 0.9548, 0.9611, 0.9637, 0.9655, 0.9680, 0.9688, 0.9689, 0.9690],
    [0.9451, 0.9534, 0.9596, 0.9621, 0.9639, 0.9664, 0.9672, 0.9673, 0.9674],
    [0.9438, 0.9520, 0.9581, 0.9606, 0.9623, 0.9648, 0.9655, 0.9656, 0.9657],
    [0.9424, 0.9505, 0.9565, 0.9589, 0.9606, 0.9630, 0.9638, 0.9639, 0.9640],
    [0.9411, 0.9490, 0.9548, 0.9572, 0.9588, 0.9612, 0.9619, 0.9620, 0.9621],
    [0.9398, 0.9474, 0.9531, 0.9554, 0.9570, 0.9593, 0.9600, 0.9601, 0.9602],
    [0.9385, 0.9458, 0.9513, 0.9535, 0.9550, 0.9573, 0.9579, 0.9580, 0.9581],
    [0.9371, 0.9442, 0.9494, 0.9515, 0.9530, 0.9551, 0.9558, 0.9559, 0.9560],
    [0.9358, 0.9425, 0.9475, 0.9495, 0.9509, 0.9529, 0.9535, 0.9536, 0.9537],
    [0.9345, 0.9408, 0.9455, 0.9473, 0.9487, 0.9506, 0.9511, 0.9512, 0.9513],
    [0.9332, 0.9390, 0.9434, 0.9451, 0.9464, 0.9481, 0.9487, 0.9487, 0.9488],
    [0.9319, 0.9372, 0.9412, 0.9428, 0.9440, 0.9456, 0.9460, 0.9461, 0.9462],
    [0.9306, 0.9354, 0.9390, 0.9404, 0.9414, 0.9429, 0.9433, 0.9434, 0.9435],
    [0.9293, 0.9335, 0.9367, 0.9379, 0.9388, 0.9401, 0.9405, 0.9405, 0.9406],
    [0.9280, 0.9316, 0.9343, 0.9353, 0.9361, 0.9372, 0.9375, 0.9375, 0.9376],
    [0.9268, 0.9296, 0.9318, 0.9326, 0.9332, 0.9341, 0.9344, 0.9344, 0.9344],
    [0.9255, 0.9276, 0.9292, 0.9298, 0.9303, 0.9309, 0.9311, 0.9311, 0.9312],
    [0.9243, 0.9256, 0.9265, 0.9269, 0.9272, 0.9276, 0.9277, 0.9277, 0.9278],
    [0.9231, 0.9235, 0.9238, 0.9239, 0.9240, 0.9241, 0.9242, 0.9242, 0.9242],
    [0.9219, 0.9213, 0.9209, 0.9208, 0.9207, 0.9205, 0.9205, 0.9205, 0.9205],
    [0.9207, 0.9192, 0.9180, 0.9176, 0.9172, 0.9168, 0.9166, 0.9166, 0.9166],
    [0.9195, 0.9169, 0.9150, 0.9142, 0.9136, 0.9128, 0.9126, 0.9126, 0.9125],
    [0.9184, 0.9147, 0.9118, 0.9107, 0.9099, 0.9088, 0.9084, 0.9084, 0.9083],
    [0.9173, 0.9123, 0.9086, 0.9071, 0.9060, 0.9045, 0.9041, 0.9040, 0.9040],
    [0.9162, 0.9100, 0.9053, 0.9034, 0.9020, 0.9001, 0.8996, 0.8995, 0.8994]]
    
    
    def C_ISA_1932_nozzle(D, Do, Re_D):
        beta = Do/D
        C = (0.9900 - 0.2262*beta**4.1
             - (0.00175*beta**2 - 0.0033*beta**4.15)*(1E6/Re_D)**1.15)
        return C
    
    Rd_values = [2E4, 3E4, 5E4, 7E4, 1E5, 3E5, 1E6, 2E6, 1E7]
    betas = [i/100. for i in range(44, 81)]
    
    for i in range(len(betas)):
        Cs_expect = Cs[i]
        beta = betas[i]
        Cs_calc = [round(C_ISA_1932_nozzle(D=1, Do=beta, Re_D=i), 4) for i in Rd_values]
        assert_allclose(Cs_expect, Cs_calc, atol=1E-4)
        
    # There were three typos in there in the values for beta of 0.77 or 0.78.
    # values: 0.9215, 0.9412, 0.9803

def test_C_long_radius_nozzle_full():
    Cs = [[0.9673, 0.9759, 0.9834, 0.9873, 0.9900, 0.9924, 0.9936, 0.9952, 0.9956],
    [0.9659, 0.9748, 0.9828, 0.9868, 0.9897, 0.9922, 0.9934, 0.9951, 0.9955],
    [0.9645, 0.9739, 0.9822, 0.9864, 0.9893, 0.9920, 0.9933, 0.9951, 0.9955],
    [0.9632, 0.9730, 0.9816, 0.9860, 0.9891, 0.9918, 0.9932, 0.9950, 0.9954],
    [0.9619, 0.9721, 0.9810, 0.9856, 0.9888, 0.9916, 0.9930, 0.9950, 0.9954],
    [0.9607, 0.9712, 0.9805, 0.9852, 0.9885, 0.9914, 0.9929, 0.9949, 0.9954],
    [0.9596, 0.9704, 0.9800, 0.9848, 0.9882, 0.9913, 0.9928, 0.9948, 0.9953],
    [0.9584, 0.9696, 0.9795, 0.9845, 0.9880, 0.9911, 0.9927, 0.9948, 0.9953],
    [0.9573, 0.9688, 0.9790, 0.9841, 0.9877, 0.9910, 0.9926, 0.9947, 0.9953],
    [0.9562, 0.9680, 0.9785, 0.9838, 0.9875, 0.9908, 0.9925, 0.9947, 0.9952],
    [0.9552, 0.9673, 0.9780, 0.9834, 0.9873, 0.9907, 0.9924, 0.9947, 0.9952],
    [0.9542, 0.9666, 0.9776, 0.9831, 0.9870, 0.9905, 0.9923, 0.9946, 0.9952],
    [0.9532, 0.9659, 0.9771, 0.9828, 0.9868, 0.9904, 0.9922, 0.9946, 0.9951],
    [0.9523, 0.9652, 0.9767, 0.9825, 0.9866, 0.9902, 0.9921, 0.9945, 0.9951],
    [0.9513, 0.9645, 0.9763, 0.9822, 0.9864, 0.9901, 0.9920, 0.9945, 0.9951],
    [0.9503, 0.9639, 0.9759, 0.9819, 0.9862, 0.9900, 0.9919, 0.9944, 0.9950],
    [0.9499, 0.9635, 0.9756, 0.9818, 0.9861, 0.9899, 0.9918, 0.9944, 0.9950],
    [0.9494, 0.9632, 0.9754, 0.9816, 0.9860, 0.9898, 0.9918, 0.9944, 0.9950],
    [0.9490, 0.9629, 0.9752, 0.9815, 0.9859, 0.9898, 0.9917, 0.9944, 0.9950],
    [0.9485, 0.9626, 0.9750, 0.9813, 0.9858, 0.9897, 0.9917, 0.9944, 0.9950],
    [0.9481, 0.9623, 0.9748, 0.9812, 0.9857, 0.9897, 0.9917, 0.9943, 0.9950],
    [0.9476, 0.9619, 0.9746, 0.9810, 0.9856, 0.9896, 0.9916, 0.9943, 0.9950],
    [0.9472, 0.9616, 0.9745, 0.9809, 0.9855, 0.9895, 0.9916, 0.9943, 0.9949],
    [0.9468, 0.9613, 0.9743, 0.9808, 0.9854, 0.9895, 0.9915, 0.9943, 0.9949],
    [0.9463, 0.9610, 0.9741, 0.9806, 0.9853, 0.9894, 0.9915, 0.9943, 0.9949],
    [0.9459, 0.9607, 0.9739, 0.9805, 0.9852, 0.9893, 0.9914, 0.9942, 0.9949],
    [0.9455, 0.9604, 0.9737, 0.9804, 0.9851, 0.9893, 0.9914, 0.9942, 0.9949],
    [0.9451, 0.9601, 0.9735, 0.9802, 0.9850, 0.9892, 0.9914, 0.9942, 0.9949],
    [0.9447, 0.9599, 0.9733, 0.9801, 0.9849, 0.9892, 0.9913, 0.9942, 0.9949],
    [0.9443, 0.9596, 0.9731, 0.9800, 0.9848, 0.9891, 0.9913, 0.9942, 0.9948],
    [0.9439, 0.9593, 0.9730, 0.9799, 0.9847, 0.9891, 0.9912, 0.9941, 0.9948],
    [0.9435, 0.9590, 0.9728, 0.9797, 0.9846, 0.9890, 0.9912, 0.9941, 0.9948],
    [0.9430, 0.9587, 0.9726, 0.9796, 0.9845, 0.9889, 0.9912, 0.9941, 0.9948],
    [0.9427, 0.9584, 0.9724, 0.9795, 0.9845, 0.9889, 0.9911, 0.9941, 0.9948],
    [0.9423, 0.9581, 0.9722, 0.9793, 0.9844, 0.9888, 0.9911, 0.9941, 0.9948],
    [0.9419, 0.9579, 0.9721, 0.9792, 0.9843, 0.9888, 0.9910, 0.9941, 0.9948],
    [0.9415, 0.9576, 0.9719, 0.9791, 0.9842, 0.9887, 0.9910, 0.9940, 0.9948],
    [0.9411, 0.9573, 0.9717, 0.9790, 0.9841, 0.9887, 0.9910, 0.9940, 0.9947],
    [0.9407, 0.9570, 0.9715, 0.9789, 0.9840, 0.9886, 0.9909, 0.9940, 0.9947],
    [0.9403, 0.9568, 0.9714, 0.9787, 0.9839, 0.9886, 0.9909, 0.9940, 0.9947],
    [0.9399, 0.9565, 0.9712, 0.9786, 0.9839, 0.9885, 0.9908, 0.9940, 0.9947],
    [0.9396, 0.9562, 0.9710, 0.9785, 0.9838, 0.9884, 0.9908, 0.9940, 0.9947],
    [0.9392, 0.9560, 0.9709, 0.9784, 0.9837, 0.9884, 0.9908, 0.9939, 0.9947],
    [0.9388, 0.9557, 0.9707, 0.9783, 0.9836, 0.9883, 0.9907, 0.9939, 0.9947],
    [0.9385, 0.9555, 0.9705, 0.9781, 0.9835, 0.9883, 0.9907, 0.9939, 0.9947],
    [0.9381, 0.9552, 0.9704, 0.9780, 0.9834, 0.9882, 0.9907, 0.9939, 0.9947]]
    
    Rd_values = [1E4, 2E4, 5E4, 1E5, 2E5, 5E5, 1E6, 5E6, 1E7]
    betas = [i/100. for i in list(range(20, 51, 2)) + list(range(51, 81))]
    
    def C_long_radius_nozzle(D, Do, Re_D):
        beta = Do/D
        return 0.9965 - 0.00653*beta**0.5*(1E6/Re_D)**0.5
    
    for i in range(len(betas)):
        Cs_expect = Cs[i]
        beta = betas[i]
        Cs_calc = [round(C_long_radius_nozzle(D=1, Do=beta, Re_D=i), 4) for i in Rd_values]
        assert_allclose(Cs_expect, Cs_calc, atol=1E-4)
    
    # Errata:
    # 0.9834 to 0.9805
    # 0.9828 to 9800
    # 0.9822 to 0.9795
    # 0.9816 to 0.979
    # 0.981 to 0.9785
    # 0.9805 to 0.9780
    # 0.98   to 0.9776
    # 0.9795 to 0.9771
    # 0.979 to 0.9767
    # 0.9785 to 0.9763
    #  9.9607 to 0.9607
    # 0.9875 to 0.9785    

def test_C_venturi_nozzle_full():
    # Many values do not match well, but the equation has been checked with both standards.
    betas = [0.32, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.40, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.50, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.60, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.70, 0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78]
    Cs = [0.9847, 0.9846, 0.9845, 0.9843, 0.9841, 0.9838, 0.9836, 0.9833, 0.9830, 0.9826, 0.9823, 0.9818, 0.9814, 0.9809, 0.9804, 0.9798, 0.9792, 0.9786, 0.9779, 0.9771, 0.9763, 0.9755, 0.9745, 0.9736, 0.9725, 0.9714, 0.9702, 0.9689, 0.9676, 0.9661, 0.9646, 0.9630, 0.9613, 0.9595, 0.9576, 0.9556, 0.9535, 0.9512, 0.9489, 0.9464, 0.9438, 0.9411, 0.9382, 0.9352, 0.9321, 0.9288, 0.9253, 0.9236]
    Cs_calc = [C_venturi_nozzle(D=1, Do=beta) for beta in betas]
    assert_allclose(Cs, Cs_calc, rtol=5E-3)



@pytest.mark.slow
def test_fuzz_K_to_discharge_coefficient():
    '''
    # Testing the different formulas
    from sympy import *
    C, beta, K = symbols('C, beta, K')

    expr = Eq(K, (sqrt(1 - beta**4*(1 - C*C))/(C*beta**2) - 1)**2)
    solns = solve(expr, C)
    [i.subs({'K': 5.2314291729754, 'beta': 0.05/0.07366}) for i in solns]
    
    [-sqrt(-beta**4/(-2*sqrt(K)*beta**4 + K*beta**4) + 1/(-2*sqrt(K)*beta**4 + K*beta**4)),
 sqrt(-beta**4/(-2*sqrt(K)*beta**4 + K*beta**4) + 1/(-2*sqrt(K)*beta**4 + K*beta**4)),
 -sqrt(-beta**4/(2*sqrt(K)*beta**4 + K*beta**4) + 1/(2*sqrt(K)*beta**4 + K*beta**4)),
 sqrt(-beta**4/(2*sqrt(K)*beta**4 + K*beta**4) + 1/(2*sqrt(K)*beta**4 + K*beta**4))]
    
    # Getting the formula
    from sympy import *
    C, beta, K = symbols('C, beta, K')
    
    expr = Eq(K, (sqrt(1 - beta**4*(1 - C*C))/(C*beta**2) - 1)**2)
    print(latex(solve(expr, C)[3]))
    '''
    
    Ds = np.logspace(np.log10(1-1E-9), np.log10(1E-9))
    for D_ratio in Ds:
        Ks = np.logspace(np.log10(1E-9), np.log10(50000))
        Ks_recalc = []
        for K in Ks:
            C = K_to_discharge_coefficient(D=1, Do=D_ratio, K=K)
            K_calc = discharge_coefficient_to_K(D=1, Do=D_ratio, C=C)
            Ks_recalc.append(K_calc)
        assert_allclose(Ks, Ks_recalc)