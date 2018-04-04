library(tidyverse)

dat <- read_csv("creditcard.csv")
sum(dat$Class)/nrow(dat)

FF <- min(which(dat$Class==1))
X <- dat[c(1:10, FF),]
l = log(nrow(X), 2)

iTree <- function(X, e, l){
  
}