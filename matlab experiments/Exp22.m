clc;
clear all;
close all;

f = @(x) cos(x)-3*x+1;

x = 0:0.01:0.5*pi;
y = feval(f,x);

plot(x,y);
xlabel('x');
ylabel('y');
grid on;

root = secant(f,1,0.0001,10);

disp('the root is:');
disp(root);