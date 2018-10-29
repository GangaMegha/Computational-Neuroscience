%THIS PROGRAM DEMONSTRATES HODGKIN HUXLEY MODEL IN CURRENT CLAMP EXPERIMENTS AND SHOWS ACTION POTENTIAL PROPAGATION
%Time is in msecs, voltage in mvs, conductances in m mho/mm^2, capacitance in uF/mm^2

% threshold value of current is 0.0223

freq = zeros(1, 200);
I = zeros(1,200);
count = zeros(1,200);

I1 = 0;
I2 = 0;
I3 = 0;
k = 1;

for ImpCur = 0:0.0005:1
    gkmax=.36;
    vk=-77; 
    gnamax=1.20;
    vna=50; 
    gl=0.003;
    vl=-54.387; 
    cm=.01; 
    
    dt=0.01;
    niter=10000;
    t=(1:niter)*dt;
    iapp=ImpCur*ones(1,niter);
    v=-64.9964;
    m=0.0530;
    h=0.5960;
    n=0.3177;
    
    gnahist=zeros(1,niter);
    gkhist=zeros(1,niter);
    vhist=zeros(1,niter);
    mhist=zeros(1,niter);
    hhist=zeros(1,niter);
    nhist=zeros(1,niter);
    
    
    for iter=1:niter
      gna=gnamax*m^3*h; 
      gk=gkmax*n^4; 
      gtot=gna+gk+gl;
      vinf = ((gna*vna+gk*vk+gl*vl)+ iapp(iter))/gtot;
      tauv = cm/gtot;
      v=vinf+(v-vinf)*exp(-dt/tauv);
      alpham = 0.1*(v+40)/(1-exp(-(v+40)/10));
      betam = 4*exp(-0.0556*(v+65));
      alphan = 0.01*(v+55)/(1-exp(-(v+55)/10));
      betan = 0.125*exp(-(v+65)/80);
      alphah = 0.07*exp(-0.05*(v+65));
      betah = 1/(1+exp(-0.1*(v+35)));
      taum = 1/(alpham+betam);
      tauh = 1/(alphah+betah);
      taun = 1/(alphan+betan);
      minf = alpham*taum;
      hinf = alphah*tauh;
      ninf = alphan*taun;
      m=minf+(m-minf)*exp(-dt/taum);
      h=hinf+(h-hinf)*exp(-dt/tauh);
      n=ninf+(n-ninf)*exp(-dt/taun);
      vhist(iter)=v; mhist(iter)=m; hhist(iter)=h; nhist(iter)=n;
    end
    
    % For plotting the frequency v/s external current
    [peaks, locs] = findpeaks(vhist);
    if length(peaks) > 2 && peaks(2) < 0
        freq(k) = 0;
    elseif length(peaks) > 2 && peaks(3) > 0
      freq(k) = 1000.0/(t(locs(3))-t(locs(2)));
    else
      freq(k) = 0;
    end
    I(k) = ImpCur;
    count(k) = length(peaks);
   
    % For computing I1, I2 and I3
    if ImpCur < 0.0224     %     Current threshold give in the code
        I1 = ImpCur;
    elseif freq(k)~=0      %   => Frequency not 0 and oscillations still +ve
        if count(k)<7      %     => Finite no. of peaks ; verified manually 
            I2 = ImpCur;
        else
            I3 = ImpCur;
        end
    end
       
    k = k + 1;
end

figure(1);
plot(I,freq,'r');
hold on;
yL = get(gca,'YLim');
line([I1 I1], yL, 'Color', 'k');
text(I1(1),-3,'I1'); 
line([I2 I2], yL, 'Color', 'g')
text(I2(1),-3,'I2'); 
line([I3 I3], yL, 'Color', 'y')
text(I3(1),-3,'I3');
xlabel('I_{ext}');
ylabel('Firing rate');
title('Frequency vs I_{ext}');