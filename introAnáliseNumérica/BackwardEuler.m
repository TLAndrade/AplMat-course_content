function BackwardEuler(h,interv,x0,y0)
t0=interv(1);
T=interv(2);
N=floor((T-t0)/h);

x=x0;
y=y0;
t=t0;

solx=[x0,zeros(1,N)];
soly=[x0,zeros(1,N)];
time=[t0,zeros(1,N)];

for i=1:N
    
    %X=x+h*f1(X,Y)-> 0=x+h*f1(X,Y)-X
    %Y=y+h*f2(Y)-> 0=y+h*f2(Y)-Y
    
    y=fzero(@(Y) y+h*f2(Y)-Y,y0);
    x=fzero(@(X) x+h*f1(X,y)-X,x0);
    
    t=t+h;
    
    solx(i+1)=x;
    soly(i+1)=y;
    time(i+1)=t;
end

%plot da solução exata x:
plot(time, exp(-1000*time)*x0-exp(-1000*time)*y0/1000+exp(-0.1*time)*x0/1000,'r')
%hold on

%plot da solução exata y:
hold on

%plot de Euler para x:
plot(time,solx,'m')
%hold on

%plot de Euler para y:
%plot(time,soly,'g')

title('Solução exata e solução por Euler de Y (h=0.001)')
legend({'solução exata','solução por Euler'},'Location','southwest')






function y=f1(x_k,y_k)
y=-1000*x_k+y_k;

function y=f2(y_k)
y=-1/10*y_k;

function Euler()