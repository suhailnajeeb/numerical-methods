clc;
clear all;
close all;

func = @(x) x.^3 - 6* x.^2 + 4*x + 12;

x = -2:0.1:6;
y = feval(func,x);

plot(x,y);
xlabel('x');
ylabel('y');
grid on;

xl = 2;
xu = 3;
es = 0.1;
imax = 10;

xr = bisect(xl,xu,es,imax,func)