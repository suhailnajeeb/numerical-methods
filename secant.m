function r = secant(f,x,es,imax)
    xr = x;
    ea = 10000;
    iter = 0;
    x0 = 0;
    fprintf('it\t\txr\t\tf(xr)\t\terror\n');
    while(ea>es && iter < imax)
        xrold = xr;
        fx0 = feval(f,x0);
        fx = feval(f,xrold);
        xr = xrold - (fx*(x0-xrold))/(fx0-fx);
        iter = iter + 1;
        if(xr ~=0)
           ea = abs((xr-xrold)/xr)*100; 
        end
        fprintf('%d \t %f \t %f \t %f \n', iter, xr, fx, ea); 
    end
    r = xr;
end