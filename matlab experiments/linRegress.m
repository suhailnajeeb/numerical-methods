clc;
clear all;
close all;

x = [1 2 3 4 5 6 7];
y = [0.22 0.5765 0.8622 2.0408 3.3265 4.0051 6.6122 ];
n = 7;

scatter(x,y);
hold on;

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

fprintf('the equation is: y = %.5f + %.5f x \n',a1,a0);

fprintf('computations for an error analysis of the linear fit: \n');
fprintf('x \t y \t \t \t st \t \t \t sr \n')

for i = 1:n
    st0 = (y(i)-ym)^2;
    sr0 = (y(i)-a1*x(i)-a0)^2;
    st = st + st0;
    sr = sr + sr0;
    fprintf('%d \t %.5f \t %.5f \t %.5f \n', x(i), y(i), st0, sr0); 
end

fprintf('-------------------------------------\n');
fprintf('%d \t %.5f \t %.5f \t %.5f \n', sumx, sumy, st, sr);

syx = (sr/(n-2))^(0.5);
r2 = (st - sr)/st;

fprintf('Sy/x = %.5f & r2 = %.5f', syx, r2);

yr = a0 + a1.*x;
plot(x,yr);