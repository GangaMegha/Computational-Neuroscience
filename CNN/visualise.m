
clear all; close all;
% Load pretrained network
load CNN_Network

%%
%Visualize weights
for i=1:20
    h=figure(i);set(h, 'Visible', 'off'); imagesc(Wc(:,:,i));pause(0.5);
    saveas(h,sprintf('Fig_weights_%d.png',i));
    h1 = figure(i+20);set(h1, 'Visible', 'off'); imagesc(Wc(:,:,i));colormap(gray);pause(0.5)
    saveas(h1,sprintf('Fig_grey_%d.png',i));
end