set.seed(123)

country_names <- c(
  "Belgium","Netherlands","France","Germany","Italy","Spain","Portugal","Austria",
  "Sweden","Norway","Denmark","Finland","Poland","Czechia","Greece","Ireland",
  "United Kingdom","Switzerland","Hungary","Turkey"
)

happy_new <- data.frame(
  Country = country_names[1:20],                 # or sample(country_names, 20)
  Freedom = runif(20, 0.2, 0.9),
  Economy = runif(20, 0.3, 1.0),
  Health  = runif(20, 0.4, 0.95)
)

head(happy_new)

cv_freedom <- sd(happy_new$Freedom) / mean(happy_new$Freedom)
cv_freedom

funCV <- function(x){
  sd(x) / mean(x)
}

funCV(happy_new$Freedom)
funCV(happy_new$Economy)

new <- sample(happy_new$Freedom, size = 50, replace = TRUE)
new

funCV(new)

BOOT <- replicate(1000, {
  new <- sample(happy_new$Freedom, size = 50, replace = TRUE)
  funCV(new)
})

head(BOOT)

library(ggplot2)
library(grid)


hist1 = ggplot(data=NULL,aes(BOOT)) +
  geom_histogram(bins=30, colour="black", fill="green")
boxplot1 = ggplot(data=NULL,aes(BOOT)) +
  geom_boxplot(colour="black",fill="blue")

grid.newpage()
pushViewport(viewport(layout=grid.layout(1,2)))
vplayout <- function(x,y){
  viewport(layout.pos.row=x, layout.pos.col=y)
}
print(hist1, vp=vplayout(1,1))
print(boxplot1, vp=vplayout(1,2))

lower = quantile(BOOT,prob=0.05)
upper = quantile(BOOT,prob=0.95)
stats = list(meanCV = mean(BOOT),
             stdCV = sd(BOOT),
             lower = quantile(BOOT,prob=0.05),
             upper = quantile(BOOT,prob=0.95))

boot_cv = function(x, sz, B){
  BOOT = c()
  for(i in 1:B){
    new = sample(x, sz, replace = TRUE)
    BOOT[i] = funCV(new)
  }
}

hist1 = ggplot(data=NULL,aes(BOOT)) +
  geom_histogram(bins=30, colour="black", fill="green")
boxplot1 = ggplot(data=NULL,aes(BOOT)) +
  geom_boxplot(colour="black",fill="blue")
grid.newpage()
pushViewport(viewport(layout=grid.layout(1,2)))
vplayout <- function(x,y){
  viewport(layout.pos.row=x, layout.pos.col=y)
}
print(hist1, vp=vplayout(1,1))
print(boxplot1, vp=vplayout(1,2))

lower = quantile(BOOT,prob=0.05)
upper = quantile(BOOT,prob=0.95)
stats = list(meanCV = mean(BOOT),
             stdCV = sd(BOOT),
             lower = quantile(BOOT,prob=0.05),
             upper = quantile(BOOT,prob=0.95))
stats

boot_cv(happy_new$Economy,70,500)
