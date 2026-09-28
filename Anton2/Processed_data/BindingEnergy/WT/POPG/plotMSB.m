function plotMSB

cd r547\
DeltaT=dlmread('IE_NORMAL_PB_Delta_TOTAL.csv',',', 1,0);
cd ../
t0=1690;
t=t0+DeltaT(:,1)*1;
En1=DeltaT(:,2);



% plot(t,En1,'-',  'LineWidth',2)
% hold on 

EL(1)=mean(En1);
sL(1)=std(En1);

cd r548\
DeltaT=dlmread('IE_NORMAL_PB_Delta_TOTAL.csv',',', 1,0);
cd ../
t0=1690;
t=t0+DeltaT(:,1)*1;
En2=DeltaT(:,2);
mean(En2)

% plot(t,En2,'-',  'LineWidth',2)

EL(2)=mean(En2);
sL(2)=std(En2);

cd r549\
DeltaT=dlmread('IE_NORMAL_PB_Delta_TOTAL.csv',',', 1,0);
cd ../
t0=1690;
t=t0+DeltaT(:,1)*1;
En3=DeltaT(:,2);

% plot(t,En3,'-',  'LineWidth',2)

EL(3)=mean(En3);
sL(3)=std(En3);


cd r550\
DeltaT=dlmread('IE_NORMAL_PB_Delta_TOTAL.csv',',', 1,0);
cd ../
t0=1690;
t=t0+DeltaT(:,1)*1;
En4=DeltaT(:,2);

% plot(t,En4,'-',  'LineWidth',2)


EL(4)=mean(En4);
sL(4)=std(En4);

cd r551\
DeltaT=dlmread('IE_NORMAL_PB_Delta_TOTAL.csv',',', 1,0);
cd ../
t0=1690;
t=t0+DeltaT(:,1)*1;
En5=DeltaT(:,2);

% plot(t,En5,'-',  'LineWidth',2)

EL(5)=mean(En5);
sL(5)=std(En5);

En=En1+En2+En3+En4+En5;

% plot(t,En1+En2+En3+En4+En5,'-',  'LineWidth',2)

Enall=mean(En)
stall=std(En)
En1av=Enall/5

 %cluster contribution
cd CBE1720\
DeltaT=dlmread('IE_NORMAL_PB_Delta_TOTAL.csv',',', 1,0);
cd ../
t0=1690;
t=t0+DeltaT(:,1)*1;
Enc=DeltaT(:,2);

Encave=mean(Enc)
stdave=std(Enc)

EL(6)=Encave;
sL(6)=stdave;

% plot(t,Enc,'-',  'LineWidth',2)

data=[Enall, Enall/5 Encave, stall, stall/5, stdave]
save('Energy.dat','data', '-ascii' )


% ylabel('\Delta G (Kcal/mol)')
% xlabel('Time(ns)')

Avfact=mean((Enc-En))
savfact=std((Enc-En))

% ESA=mean(En1+En2+En5);
% SSA=std(En1+En2+En5);
% 
% ESB=mean(En3+En4);
% SSB=std(En3+En4);
% 
% decomp=[ESA ESB SSA SSB]
% save("Energydecomp.dat", "decomp", '-ascii')

figure

l=1:6;
ligand={'POPG1', 'POPG2', 'POPG3', 'POPG4','POPG5', 'Total'};

b=bar(l,EL,'FaceColor','g', EdgeColor='none')
colors=[
     0.7 0.3 0.3;   % 
     0.7 0.3 0.3;    % 
     0.7 0.3 0.3;    %
     0.7 0.3 0.3;  % sbsA
     0.7 0.3 0.3; % 
     0.5 0.5 0.5; % 
];
%legend('SBS A', 'Location','northwest')
%legend boxoff 

b.CData = colors;    % assign colors
b.FaceColor = 'flat';
hold on
errorbar(l,EL, sL,'.', 'LineWidth',1)
ax = gca;
ax.YDir = 'reverse'
ax.XTickLabel = ligand;
xtickangle(45)
ylabel('\Delta H (Kcal/mol)')
ylim([-200 0])
xlim([0.5 6.5])
box off


ax.LineWidth=1.5;
ax.FontSize=15;
fig1=gcf;
fig1.PaperUnits= 'inches';
fig1.PaperPosition = [0 0 6 4 ]
print(fig1,'MSB', '-dtiff','-r600')
