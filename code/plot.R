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


# plot2 -------------------------------------------------------------------

y1 = c(0.0, 0.01, 0.0055, 0.0034, 0.0152, 0.01165, 0.01166, 0.00909)
y2 = c(0, 0.01, 0.005, 0.003, 0.019, 0.02125, 0.0148, 0.01115)
x = c(500, 1000, 2000, 5000, 10000, 20000, 50000, 100000)
dat2 = tibble(
  x = rep(log10(x), 2),
  y = c(y1, y2),
  index = c(rep('MSE', 8), rep('5*fraud proportion', 8))
)
dat2 %>%
  ggplot() +
  geom_line(aes(x, y, color = index)) +
  xlab("log10 of data size")
  


