% This code will take in a jpg image and create a Phase scrambled image
%
% source: http://visionscience.caom/pipermail/visionlist/2007/002181.html

% Clear workspace 
clc
clear 
cd('/Users/feusn/Desktop/VMphotos/improc/natural/')
files(1).in='1.jpg'; files(1).out='5.jpg';
files(2).in='2.jpg'; files(2).out='6.jpg';
files(3).in='3.jpg'; files(3).out='7.jpg';
files(4).in='4.jpg'; files(4).out='8.jpg';
files(5).in='11.jpg'; files(5).out='15.jpg';
files(6).in='12.jpg'; files(6).out='16.jpg';
files(7).in='13.jpg'; files(7).out='17.jpg';
files(8).in='14.jpg'; files(8).out='18.jpg';

for i=1:8
    ImageName=files(i).in;
    OutputName=files(i).out;
    %% Actual Code portion
    %read and rescale (0-1) image
    Im = imread(ImageName);
    Im = im2double(Im);
    Im = mat2gray(Im);

    % Calculate image size
    ImSize = size(Im);

    % Generate random phase structure
    RandomPhase = angle(fft2(rand(ImSize(1), ImSize(2))));


    for layer = 1:ImSize(3)
        %Fast-Fourier transform
        ImFourier(:,:,layer) = fft2(Im(:,:,layer));

        %amplitude spectrum
        Amp(:,:,layer) = abs(ImFourier(:,:,layer));

        %phase spectrum
        Phase(:,:,layer) = angle(ImFourier(:,:,layer));

        %add random phase to original phase
        Phase(:,:,layer) = Phase(:,:,layer) + RandomPhase;

        %combine Amp and Phase then perform inverse Fourier
        ImScrambled(:,:,layer) = ifft2(Amp(:,:,layer).*exp(sqrt(-1)*(Phase(:,:,layer))));

    end

    %get rid of imaginery part in image (due to rounding error)
    ImScrambled = real(ImScrambled);

    % Save image as ImageOuputName
    imwrite(ImScrambled,OutputName,'jpg');

    % Display the scrambled image
    imshow(ImScrambled)
end
cd('/Users/feusn/Desktop/VMphotos/scripts/')