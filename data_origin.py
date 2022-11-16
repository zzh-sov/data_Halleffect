import numpy as np
import matplotlib.pyplot as plt
#t:样品摄氏温度
t=np.array([28.7,37.7,46.7,55.5,64.5,73.9,83.8,91.9,
            98.0,104.8,111.0,117.6,124.4,130.2,132.6,135.4,138.3,141.2,144.2,147.2,150.0,154.8])
#对应于测量量V1(I)，单位为V
V1=np.array([0.2461,0.2780,0.3041,0.3289,0.3523,0.3661,
             0.3620,0.3192,0.2704,0.2016,0.1456,0.1002,
             0.0710,0.0550,0.0497,0.0445,0.0394,0.0352,0.0312,.0282,.0253,.0218])
#对应于测量量V2(I)，单位为V
V2=np.array([1.3475,1.4837,1.5864,1.6752,1.7428,1.7586,
             1.6958,1.4851,1.2648,0.9768,0.7231,0.5139,
             0.3704,0.2914,0.2642,0.2370,0.2112,0.1891,0.1691,.1535,.1378,.1191])
#对应于测量量V1(-I)，单位为V
Vm1=np.array([-0.2461,-0.2769,-0.3029,-0.3285,-0.3521,
              -0.3660,-0.3621,-0.3193,-0.2730,-0.2077,
              -0.1548,-0.1066,-0.0736,-0.0562,-0.0504,-0.0449,-0.0397,-0.0353,-.0313,-.0283,-.0252,-.0217])
#对应于测量量V2(I)，单位为V
Vm2=np.array([-1.3472,-1.4823,-1.5844,-1.6750,-1.7454,
              -1.7665,-1.7130,-1.5047,-1.2778,-0.9760,
              -0.7201,-0.5151,-0.3735,-0.2934,-0.2656,-0.2383,-0.2121,-0.1900,-.1695,-.1539,-.1380,-.1193])
#对应于测量量V3(I,0)，单位为V
V3pB0=np.array([-1.1148,-1.2168,-1.2921,-1.3560,-1.4017,
                -1.4027,-1.3434,-1.1728,-0.9988,-0.7859,
                -0.5707,-0.4073,-0.2952,-0.2330,-0.2114,-0.1897,-0.1694,-0.1518,-.1359,-.1235,-.1111,-.0959])
#对应于测量量V3(I,B)，单位为V
V3pBp=np.array([-1.0658,-1.1680,-1.2436,-1.3105,-1.3600,
                -1.3692,-1.3260,-1.1741,-1.0082,-0.7990,
                -0.5900,-0.4280,-0.3117,-0.2465,-0.2240,-0.2008,-0.1793,-0.1605,-.1442,-.1307,-.1176,-.1014])
#对应于测量量V3(-I,0)，单位为V
V3nB0=np.array([1.1151,1.2152,1.2893,1.3550,1.4002,
                1.4010,1.3414,1.1717,1.0027,0.7981,
                0.5893,0.4217,0.3011,0.2360,0.2138,0.1912,0.1706,0.1525,.1368,.1240,.1116,.0962])
#对应于测量量V3(-I,-B)，单位为V
V3nBn=np.array([1.1405,1.2393,1.3126,1.3775,1.4225,
                1.4236,1.3633,1.1907,1.0160,0.8061,
                0.5920,0.4194,0.2960,0.2309,0.2089,0.1866,0.1664,0.1486,.1335,.1209,.1087,.0937])
