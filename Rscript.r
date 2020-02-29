f="out.data"
data=read.table(f)
attach(data)
A=V1
B=V2
plot(A,xlab="iteration",ylab="probilité de stratégie",col="red",type='l',xlim=c(1,50000))
lines(B,xlab="iteration",ylab="p",col="blue",xlim=c(1,50000))

f="outp.data"
detach(data)
data=read.table(f)
attach(data)
A=V1
B=V2
plot(A,xlab="iteration",ylab="probilité de stratégie",col="red",type='l',xlim=c(1,50000),ylim=c(0,1))
lines(B,xlab="iteration",ylab="p",col="blue",xlim=c(1,50000))


