#=============默认速度 步长 设置=============
#机器人物理参数设置
l1=80     #大腿长(mm)
l2=62.5   #小腿长(mm)
ma_case=0 #舵机安装方式选项（0：标准装法 1：侧装）

"""
     \\         |
 o=====o        |
o     o         |  
 o     o   _____|______
    起点 终点   - 0 +     
"""
#步态参数设置 #前进步态终点 #后退步态终点
xf_f=40    #前进步态起点

xs_f=-0   #前进步态终点 -10

xf_b=6    #后退步态终点
xs_b=-15   #后退步态起点

xf_l=20    #左转步态终点
xs_l=-15   #左转步态起点
xf_r=20    #右转步态终点
xs_r=-15   #右转步态起点

h=50    #抬腿高度 设置

speed=0.025  #步频调节
sp_goal=0.025

#跳跃参数设置
prep_time = 0.3      #跳跃准备时间
launch_time = 0.5    #跳跃持续时间
fall_time = 0.4      #下降持续时间
stance_height = 80   #跳前收腿长度(mm)
jump_extension = 110 #跳时腿伸张长度(mm)
fall_extension = 70  #下降时腿长度(mm)
x_jump=-40           #x初始起跳位置

#=============一般不改变量=============
xf=40   #默认步态终点坐标（一般不改）
xs=15  #默认步态起点坐标（一般不改）
Ts=1   #周期
faai=0.5   #占空比

#=============默认舵机中位值设置=============
#狗腿子顺序(从1开始顺时针数)
#===头===
#1==-==2
#4==-==3
init_1h = 108   #1脚大腿
init_1s = 95   #1脚小腿

init_2h = 75   #2脚大腿
init_2s = 97  #2脚小腿

init_3h = 97   #3脚大腿
init_3s = 110   #3脚小腿

init_4h = 85   #4脚大腿
init_4s = 107   #4脚小腿

#=============PCA9685舵机控制板=============
#pcai2c = I2C(scl='Y9', sda='Y10', freq=100000)

#=============调节比例系数=============
Kp_H=0.07   #高度调节系数
Kp_G=0.07   #姿态调节系数
#=============一些中间变量=============
t=0
init_x=0
init_y=-100   #初始机器人高度(mm)
x1=init_x
y1=init_y
x2=init_x
 
y2=init_y
x3=init_x
y3=init_y
x4=init_x
y4=init_y

ges_x_1=0
ges_x_2=0
ges_x_3=0
ges_x_4=0

ges_y_1=init_y
ges_y_2=init_y
ges_y_3=init_y
ges_y_4=init_y