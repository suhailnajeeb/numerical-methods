function r = fixpt(g,x0,es,imax)
    xr = x0;
    ea = 10000;
    iter = 0;
    while(ea>es || iter <= imax)
        xrold = xr;
        xr = feval(g,xrold);
        iter = iter + 1;
        if(xr ~=0)
           ea = abs((xr-xrold)/xr)*100; 
        end      
    end
    r = xr;
end