d = textread('../work/out');
Fs = 6.144e9;
sL = 61440;
ol = 32000;
nfft = 61440;

[pxx,f] = pwelch(d,sL,ol,nfft,Fs);
plot(f,10*log10(pxx));

