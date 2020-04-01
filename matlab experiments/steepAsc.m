% Steepest ascent algorithm on the function f(x,y) = 2xy + 2x - x^2 -2y^2 

% Initialize Matlab

clc;
close all;
clear all;

% Declare function

func = @(x,y) 2.*x.*y + 2.*x - x.^2 - 2.*y.^2;

% Declare Derivatives


x = linspace(-5,5,100);
y = linspace(-5,5,100);

[Y,X] = meshgrid(y,x);
F = func(X,Y);
%surf(x,y,F');
%shading interp;

%dfdx = @(x,y) 2*y + 2 - 2*x;
%dfdy = @(x,y) 2*x - 4*y;

% Initial Guess

x0 = 1;
y0 = 1;

% Algorithm Parameters

dx = 0.001;
dy = 0.001;
alpha = 0.1;

tol = 1e-3;
g = [inf,inf];

while norm(g) > tol
    % Visualize
    
    imagesc(x,y,F');
    axis equal tight;
    drawnow;
    hold on;
    plot(x0,y0,'ok');
    hold off;
    pause(0.1);
    
    % Calculate Gradients
    
    f1 = func(x0-dx/2,y0);
    f2 = func(x0+dx/2,y0);
    gx = (f2-f1)/dx;
    
    f1 = func(x0,y0-dy/2);
    f2 = func(x0,y0+dy/2);
    gy = (f2-f1)/dy;
        
    g = [gx; gy];
    
    % Update position of Guess
    x0 = x0 + alpha*gx;
    y0 = y0 + alpha*gy;
    
end

% Report the answer

[x0, y0]