function RK4(h,T,k,a,b)
t0=0;
N=floor((T-t0)/h);

x0=0;
x=x0;
t=t0;

sol=[x0,zeros(1,N)];
time=[t0,zeros(1,N)];

f=@(x) (k*(a-x)*(b-x));

for i=1:N
    k1 = f(x);
    k2 = f(x+0.5*h*k1);
    k3 = f(x+0.5*h*k2);
    k4 = f(x+h*k3);
    x = x +((k1+2*k2+2*k3+k4)/6)*h;
    
    sol(i+1)=x;
    t=t+h;
    time(i+1)=t;
end

%exact solution:
plot(time,350*(1-exp(-0.2*time))./(7-5*exp(-0.2*time)),'r')
hold on

%solution by RK4:
plot(time,sol,'b')


title('Solução exata e solução por RK4')
legend({'solução exata','solução por RK4'},'Location','southwest')



   

