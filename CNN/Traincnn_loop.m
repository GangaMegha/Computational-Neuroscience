%%% This is used to loop over values of hyperparameters : No. of Epochs, No. of filters
%%% and Filter size to study the variation in Accuracy and Training Time
%%% ====================================================================================

clear all; close all;

%%%% Setting the network Configuration
%%%% ===============================
imageDim = 28;
numClasses = 10;            % Number of classes (MNIST images fall into 10 classes)
filterDim = [3,5,11];       % Filter size for conv layer
numFilters = [16,25,36];    % Number of filters for conv layer
poolDim = 2;                % Pooling dimension, (should divide imageDim-filterDim+1)
epochs = [5,10,20];


for num3 = 1:3      % Over Epochs
  for num2 = 1:3    % Over No. of Filters
    for num1 = 1:3  % Over Filter size

        %%
        % Load MNIST Train data
        %==========================
        images = loadMNISTImages('Dataset/train-images.idx3-ubyte');

        images = images(:,:,1:1000);  % Consider only first 10000 images for training 
        TrainLabels = loadMNISTLabels( 'Dataset/train-labels.idx1-ubyte');
        labels = 0.*ones(numClasses, size(TrainLabels,1)); %Train_labels is a column vector

        for n = 1: size(TrainLabels, 1)
            labels(TrainLabels(n) + 1, n) = 1;
        end;

        labels=labels(:,1:1000);
        clear TrainLabels;

        %%
        % Initialize network weights and params
        % ======================================
        [Wc,Wd,bc,bd] = cnnInitParams1(imageDim,filterDim(num1),numFilters(num2),poolDim,numClasses);


        mom = 0;
        alpha = 1e-1;
        vel_Wc = zeros(size(Wc));
        vel_Wd = zeros(size(Wd));
        vel_bc = zeros(size(bc));
        vel_bd = zeros(size(bd));

        %%
        % Actual training
        %=====================
        for e = 1:epochs(num3)
            tic;
            startTime = tic();
            %Forward Propagation
            fprintf('epoch:  %d',e);
            numImages = size(images,3);
            
            for i= 1: numImages
                im=images(:,:,i)/255;
                %fprintf('Currently training:  Epoch: %d ; Sample: %d / %d\n', e, i,numImages);

                %%% Convolution Layer
                convDim = imageDim-filterDim(num1)+1; % dimension of convolved output
                activations = zeros(convDim,convDim,numFilters(num2));
                activations = cnnConvolve2(filterDim(num1), numFilters(num2), im, Wc, bc);

                %%%% Pooling Layer
                outputDim = (convDim)/poolDim; % dimension of subsampled output
                activationsPooled1 = zeros(outputDim,outputDim,numFilters(num2));
                activationsPooled1 = cnnPool2(poolDim, activations);

                % input to fully connected layer
                activationsPooled = reshape(activationsPooled1,1,[]);
                clear activationsPooled1;
                probs = zeros(numClasses,1);
                probs = Softmax(Wd*activationsPooled' + bd);

                %Calculate Gradients
                Wc_grad = zeros(size(Wc));
                Wd_grad = zeros(size(Wd));
                bc_grad = zeros(size(bc));
                bd_grad = zeros(size(bd));

                groundTruth =labels(:,i);
                deriv_1 = -(groundTruth - probs);

                Wd_grad = deriv_1*activationsPooled;
                bd_grad = deriv_1;

                deriv_2_pooled_sh = Wd'*deriv_1;

                deriv_2_pooled = reshape(deriv_2_pooled_sh,outputDim,outputDim,numFilters(num2));
                deriv_2_upsampled = zeros(convDim,convDim,numFilters(num2));

                for filterNum = 1:numFilters(num2)

                    aux3 = (1/(poolDim^2)).*kron(squeeze(deriv_2_pooled(:,:,filterNum)),ones(poolDim));
                    deriv_2_upsampled(:,:,filterNum) = aux3.*activations(:,:,filterNum).*(1-activations(:,:,filterNum));

                    f_now = squeeze(deriv_2_upsampled(:,:,filterNum));
                    noww = conv2(im,rot90(squeeze(f_now),2),'valid');

                    Wc_grad(:,:,filterNum) = squeeze(Wc_grad(:,:,filterNum)) + noww; 
                    bc_grad(filterNum) = bc_grad(filterNum) + sum(f_now(:));
               
                end
                clear f_now; clear noww;clear aux3;
             
                %update weights along with momentum and learning rate
                vel_Wc  = (mom.* vel_Wc) + (alpha .* Wc_grad);
                Wc = Wc - vel_Wc;
                vel_Wd = (mom.* vel_Wd) + (alpha .* Wd_grad);
                Wd = Wd - vel_Wd;
                vel_bc = (mom.* vel_bc) + (alpha .* bc_grad);
                bc = bc -   vel_bc;
                vel_bd = (mom.* vel_bd) + (alpha .* bd_grad);
                bd = bd - vel_bd;   
            end;

            alpha = alpha/2.0;

        end

        toc;
        fprintf('...Done. Training took %.2f seconds\n', toc(startTime));


        %%
        % Test the trained network
        % ===========================
        accuracy = testcnn(Wc,Wd,bc,bd,imageDim,filterDim(num1),poolDim,numFilters(num2),numClasses);
        fprintf('Accuracy is: %f%%\n',accuracy*100);
    end;
  end;
end;