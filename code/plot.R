library(tidyverse)
library(gridExtra)

N = 50
set.seed(1234)
x = rnorm(N)
y = rnorm(N)
index = which.max(x)

dat = tibble(x=x,y=y)

p1 <- dat %>%
  ggplot(aes(x, y)) +
  geom_point() +
  geom_point(aes(x[index], y[index]), color='red') +
  geom_vline(aes(xintercept=2)) +
  geom_text(aes(x[index], 0.6), label='x0', color='grey50')

k = 30
p2 <- dat %>%
  ggplot(aes(x, y)) +
  geom_point() +
  geom_point(aes(x[k], y[k]), color='red') +
  geom_vline(aes(xintercept=-1)) +
  geom_vline(aes(xintercept=-0.6)) +
  geom_hline(aes(yintercept=-0.2)) +
  geom_hline(aes(yintercept=-0.4)) +
  geom_text(aes(-1.2, 0), label='x1', color='grey50')

grid.arrange(p1, p2, ncol=2)






