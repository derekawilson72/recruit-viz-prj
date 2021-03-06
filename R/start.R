
install.packages("RSQLite")
install.packages("ggplot2")

library("RSQLite")
library(ggplot2)

setwd("~/Python/recruit-viz/R/")

drv <- dbDriver("SQLite")
connection = dbConnect(drv=drv, dbname="../recruit.db")

#alltables = dbListTables(connection)
#alltables

query <- 'select * from customer'
df_customer = dbGetQuery(connection, query)

#head(df_customer)

p <- ggplot(df_customer, aes(income))
p <- p + geom_histogram(bins=50)
p

dbDisconnect(connection)
