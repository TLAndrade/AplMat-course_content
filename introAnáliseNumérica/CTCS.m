function CTCS ( )
dx=0.04;
dt=0.02;
x_interv=[-10 10];
t_interv=[0 40];
c=1;

Nx=floor((x_interv(2)-x_interv(1))/dx);
Nt=floor((t_interv(2)-t_interv(1))/dt);
sigma=c*(dt/dx);
d=2-2*sigma^2;

A=diag(d*ones(1,Nx-1))+diag(sigma^2*ones(1,Nx-2),1)+diag(sigma^2*ones(1,Nx-2),-1);

x=linspace(x_interv(1),x_interv(2),Nx+1);
t=linspace(t_interv(1),t_interv(2),Nt+1);
U0=exp(-x(2:Nx).^2)';
UL=zeros(Nx-1,1);
U_t=zeros(Nx-1,1);
U1=U0+U_t*dt; %via_1

IF=zeros(Nx-1,1);

Ui=U1;
Ui_1=U0;

plot3(x(2:Nx)',0*ones(Nx-1,1),U0,'b')
hold on
plot3(x(2:Nx)',(0+dt*1)*ones(Nx-1,1),U0,'b')

aux=0;
for i=2:Nt
    U=A*Ui+IF-Ui_1;
    Ui_1=Ui;
    Ui=U;
   
    if aux<10
        aux=aux+1;
        plot3(x(2:Nx),(0+dt*i)*ones(Nx-1,1),U,'b');
    else if aux<20
            aux=aux+1;
            plot3(x(2:Nx),(0+dt*i)*ones(Nx-1,1),U,'g');
        else 
            aux=0;
        end
    end
            
end
xlabel('X')
ylabel('t')
zlabel('u(x,t)')
    
    

