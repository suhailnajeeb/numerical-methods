function r = bisect(xl,xu,es,imax,f)
    iter = 0;
    ea = 10000;
    xr = xl;
    fprintf("iter \t\t xl \t\t xu \t\t xr \t\t ea");
    while (ea > es && iter <= imax)
        xrold = xr;
        xr = (xl+xu)/2;
        iter = iter+1;
        if(xr ~= 0)
            ea = abs((xr-xrold)/xr)*100;
        end
        fxl = feval(f,xl);
        fxr = feval(f,xr);
        test = fxl*fxr;
        
        if(test<0)
            xu = xr;
        elseif( test>0)
            xl = xr;
        else
            ea = 0;
        end
        fprintf("%d \t %f \t %f \t %f \t %f \n",iter, xl, xu, xr, ea);
        
    end
    r = xr;
end
