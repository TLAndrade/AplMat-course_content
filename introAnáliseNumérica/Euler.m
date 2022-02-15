function Euler(interv, x0, h)
t0=interv(1);
T=interv(2);
N=floor((T-t0)/h);

x=x0;
t=t0;

sol=[x0,zeros(1,N)];
time=[t0,zeros(1,N)];

for i=1:N
    x=x+h*f(t,x);%Euler
    t=t+h;
    
    sol(i+1)=x;
    time(i+1)=t;
end
%plot da solução exata:
plot(time, 1./(time.^4+1),'r')

hold on
%plot de Euler:
plot(time,sol,'b')


    
%definição da função
function y=f(t,x)
y=-4*t^3*x^2;