% f(x) = 2sin(x) - x^2/10
% f'(x) = 2cos(x) - x/5
% f''(x) = -2sin(x) - x/10

% iterative method: x(i+1) = x(i) - f'(x(i))/f''(x(i))

clc;
clear all;
close all;

f = @(x) 2*sin(x) - x^2/10;
df = @(x) 2*cos(x) - x/5;
ddf = @(x) -2*sin(x) - x/10;

x = 2.5;
iter = 0;
imax = 25;
es = 0.000001;
DF = 10000;

fprintf("iter \t\t x \t\t f(x) \t\t f'(x) \t\t f''(x) \n");

while(abs(DF)>es && iter < imax)
    F = feval(df, x);
    DF = feval(df,x);
    DDF = feval(ddf,x);
    x = x - DF/DDF;
    iter = iter + 1;
    fprintf("%d \t %f \t %f \t %f \t %f \n", iter, x, F, DF, DDF);
end