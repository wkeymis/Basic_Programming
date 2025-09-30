set.seed(123)

drug <- data.frame(
  id      = 1:24,                                # 24 observations
  initial = rep(1:3, each = 8),                  # values 1, 2, 3
  dosage  = rep(1:4, times = 6),                 # values 1, 2, 3, 4
  leverPR = round(rnorm(24, mean = 70, sd = 15), 1)  # continuous variable
)

head(drug)

install.packages("doBy")
library(doBy)

result_sum <- data.frame(
  summaryBy(leverPR ~ dosage + initial, data = drug, FUN = c(mean,sd))
)

final <- merge(drug, result_sum,
               by.x = c("dosage", "initial"),
               by.y = c("dosage", "initial")
               )
head(final, 20)

fun1 <- function(x_cont, y_cat){
  med <- median(x_cont, na.rm = TRUE)
  x_cat <- ifelse(x_cont <= med, "low", "high")
  tbl <- table(x_cat, y_cat)
  pval <- chisq.test(tbl)$p.value

  cat("This is a test for independence\n")
  list(
    table = tbl,
    pvalue = pval
  )
}

fun1(drug$leverPR, drug$dosage)

library(ggplot2)

plot1 <- ggplot(drug, aes(x = initial, y = leverPR)) +
  geom_point(color = "red") +
  scale_x_continuous(limits = c(1, 3))

plot2 <- plot1 + facet_wrap(~dosage)

plot3 <- plot2 +
  stat_summary(fun = mean, geom = "point", color = "blue", size = 5)

plot4 <- plot3 +
  ggtitle("Average LeverPR by initial: each panel has different dosage")
plot1
plot2
plot4
