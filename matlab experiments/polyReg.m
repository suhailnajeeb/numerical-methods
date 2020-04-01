clc;
clear all;
close all;

m = 2;
n = 6;

x = [0 1 2 3 4 5];
y = [2.1 7.7 13.6 27.2 40.9 61.1];

xm = mean(x);
ym = mean(y);

XI = [];
for j = 1:2*m+1
    sum = 0;
    for i=1:n
        sum = sum + power(x(i),j-1);
    end
    XI(j) = sum;
end

XIYI = [];
for j = 1:m+1
    sum = 0;
    for i=1:n
        sum = sum + power(x(i),j-1)*y(i);
    end
    XIYI(j) = sum;
end

A = zeros(m+1,m+1);
idx = 1;
for i = 1:m+1
    for j = 1:m+1
        A(idx) = XI(i+j-1);
        idx = idx + 1;
    end
end

B = transpose(XIYI);

n = 3;

% Forward Elimination

for k = 1:n-1
   for i = k+1: n
       factor = A(i,k)/A(k,k);
       for j = 1 : n
           A(i,j) = A(i,j)-factor*A(k,j);
       end
       B(i) = B(i)-factor*B(k);
   end
end

% Back Substitution

X = zeros(1,n);

X(n) = B(n)/A(n,n);

for i = n-1:-1:1
    sum = B(i);
    for j = i+1:n
        sum = sum - A(i,j)*X(j);
    end
    X(i) = sum/A(i,i);
end

disp(X)

