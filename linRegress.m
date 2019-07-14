clc;
clear all;
close all;

x = [1 2 3 4 5 6 7];
y = [8.5765 0.8622 2.0408 0.3265 0.0051 6.6122 4.2908];
n = 7;

plot(x,y);

sumx = 0;
sumy = 0;
sumxy = 0;
sumx2 = 0;
st = 0;
sr = 0;

for i = 1:n
    sumx = sumx + x(i);
    sumy = sumy + y(i);
    sumxy = sumxy + x(i)*y(i);
    sumx2 = sumx2 + x(i)*x(i);
end

xm = sumx/n;
ym = sumy/n;

a1 = (n*sumxy-sumx*sumy)/(n*sumx2-sumx*sumx);
a0 = ym - a1*xm;


for i = 1:n
    st = st + (y(i)-ym)^2;
    sr = sr + (y(i)-a1*x(i)-a0)^2;
end

syx = (sr/(n-2))^(0.5);
r2 = (st - sr)/st;