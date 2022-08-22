#LOADING PACKAGES AND DATA
#library(plyr)
library(dplyr)
library(tidyr)
#library(tidyverse)
library(psych)
library(ggplot2)
#library(readr)
library(ggpubr)
#library(stats)
#library(agricolae)
library(gridExtra)
library(rstatix)
#library(writexl)
library(stats)
library(superb)

dataset <- read.csv("C:/Users/User/Desktop/teza/Triangle 2/data/main exp data/for Beh&ET analyses/dibs/merging_outside_r/merged_avg.csv", sep = ',')
names(dataset) <- c("ppNum","NrmzMeanConfPair","NrmzMeanConfEvent","NrmzMeanConfDetail","iEvent","iBlock")
View(dataset)

#RECODING VARIABLES
dataset$iEvent = as.numeric(dataset$iEvent)
dataset$iEvent <- ifelse(dataset$iBlock == 2, dataset$iEvent - 15, 
                         ifelse(dataset$iBlock == 3, dataset$iEvent - 30,
                                ifelse(dataset$iBlock == 4, dataset$iEvent - 45,
                                       dataset$iEvent)))
dataset$iEvent = as.numeric(dataset$iEvent)
#write.csv(dataset)
#write_xlsx(dataset,"C:/Users/User/Desktop/dibs/merging_outside_r//event_restart.xlsx")

dataset = dataset %>%
  mutate(iBlock = factor(iBlock, levels = c("1","2","3","4")))
dataset = dataset %>%
  mutate(iEvent = factor(iEvent, levels = c("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15")))
dataset$NrmzMeanConfPair = as.numeric(dataset$NrmzMeanConfPair)
dataset$NrmzMeanConfEvent = as.numeric(dataset$NrmzMeanConfEvent)
dataset$NrmzMeanConfDetail = as.numeric(dataset$NrmzMeanConfDetail)

#dataframe_means <- dataset %>%
  #select(NrmzMeanConfPair, NrmzMeanConfEvent, NrmzMeanConfDetail)
#mean(dataframe_means$NrmzMeanConfPair) 
#mean(dataframe_means$NrmzMeanConfEvent) 
#mean(dataframe_means$NrmzMeanConfDetail)

#ERRORPLOT GRAPHS
ggerrorplot1 <- ggerrorplot(dataset, x = "iBlock", y = "NrmzMeanConfPair", 
            desc_stat = "mean_sd", error.plot = "errorbar",  
            add = "mean")

ggerrorplot2 <- ggerrorplot(dataset, x = "iEvent", y = "NrmzMeanConfPair", 
            desc_stat = "mean_sd", error.plot = "errorbar",  
            add = "mean")

ggerrorplot3 <- ggerrorplot(dataset, x = "iBlock", y = "NrmzMeanConfEvent", 
            desc_stat = "mean_sd", error.plot = "errorbar",  
            add = "mean")
ggerrorplot4 <- ggerrorplot(dataset, x = "iEvent", y = "NrmzMeanConfEvent", 
            desc_stat = "mean_sd", error.plot = "errorbar",  
            add = "mean")

ggerrorplot5 <- ggerrorplot(dataset, x = "iBlock", y = "NrmzMeanConfDetail", 
            desc_stat = "mean_sd", error.plot = "errorbar",  
            add = "mean")
ggerrorplot6 <- ggerrorplot(dataset, x = "iEvent", y = "NrmzMeanConfDetail", 
            desc_stat = "mean_sd", error.plot = "errorbar",  
            add = "mean")

grid.arrange(ggerrorplot1, ggerrorplot3, ggerrorplot5, nrow = 1)
grid.arrange(ggerrorplot2, ggerrorplot4, ggerrorplot6, nrow = 1)

#ANOVAS
#anova_pair1 <- aov(NrmzMeanConfPair ~ iBlock + iEvent, 
                  #data = dataset)
#anova_event1 <- aov(NrmzMeanConfEvent ~ iBlock + iEvent, 
                   #data = dataset)
#anova_detail1 <- aov(NrmzMeanConfDetail ~ iBlock + iEvent, 
                    #data = dataset)

#summary(anova_pair1)
#summary(anova_event1)
#summary(anova_detail1)

dataset = dataset %>%
  mutate(ppNum = factor(ppNum, levels = c("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29")))

res.aovP <- anova_test(
  data = dataset, dv = NrmzMeanConfPair, wid = ppNum, 
  within = c(iBlock, iEvent))
get_anova_table(res.aovP)
res.aovP$'Sphericity Corrections'

res.aovE <- anova_test(
  data = dataset, dv = NrmzMeanConfEvent, wid = ppNum, 
  within = c(iBlock, iEvent))
get_anova_table(res.aovE)
res.aovE$'Sphericity Corrections'

res.aovD <- anova_test(
  data = dataset, dv = NrmzMeanConfDetail, wid = ppNum, 
  within = c(iBlock, iEvent))
get_anova_table(res.aovD)
res.aovD$'Sphericity Corrections'

#sphericity
NrmzMeanConfPair_obj <- dataset$NrmzMeanConfPair
NrmzMeanConfEvent_obj <- dataset$NrmzMeanConfEvent
NrmzMeanConfDetail_obj <- dataset$NrmzMeanConfDetail

vectorP <- c("NrmzMeanConfPair")
vectorP <- c("NrmzMeanConfEvent")
vectorP <- c("NrmzMeanConfDetail")
dataset$NrmzMeanConfPair = as.numeric(dataset$NrmzMeanConfPair)
dataset$NrmzMeanConfEvent = as.numeric(dataset$NrmzMeanConfEvent)
dataset$NrmzMeanConfDetail = as.numeric(dataset$NrmzMeanConfDetail)

MauchlySphericityTest(dataset, NrmzMeanConfPair)

get_anova_table(res.aovP, correction = "GG")
get_anova_table(res.aovE, correction = "GG")
get_anova_table(res.aovD, correction = "GG")

get_anova_table(res.aovP, correction = "HF")
get_anova_table(res.aovE, correction = "HF")
get_anova_table(res.aovD, correction = "HF")

#MORE DETAIL - LINEAR MODELS
#mod_pair <- lm(NrmzMeanConfPair ~ iBlock + iEvent, data = dataset)
#mod_event <- lm(NrmzMeanConfEvent ~ iBlock + iEvent, data = dataset)
#mod_detail <- lm(NrmzMeanConfDetail ~ iBlock + iEvent, data = dataset)
#summary(mod_pair)
#summary(mod_event)
#summary(mod_detail)

#MAKING DATA FRAME WITH MEMORY SCORES AND FIXATION SUMMARIES
dataset = dataset %>%
  mutate(Refi = factor(Refi),
         ppNum = factor(ppNum))

x <- tapply(dataset$Refi, dataset$PPno, summary, simplify = T)
y <- data.frame(x[["1"]], x[["2"]], x[["3"]], x[["4"]], x[["5"]],
                x[["6"]], x[["7"]], x[["8"]], x[["9"]], x[["10"]],
                x[["11"]], x[["12"]], x[["13"]], x[["14"]], x[["15"]],
                x[["16"]], x[["17"]], x[["18"]], x[["19"]], x[["20"]],
                x[["21"]], x[["22"]], x[["23"]], x[["24"]], x[["25"]],
                x[["26"]], x[["27"]], x[["28"]], x[["29"]])
y = t(y)
dataset3 <- dataset %>%
  filter(NrmzMeanConfAll != "NA") %>%
  group_by(PPno) %>%
  summarise_at(vars(NrmzMeanConfPair, NrmzMeanConfEvent, NrmzMeanConfDetail, NrmzMeanConfAll), list(name = mean))
dataset3 <- cbind(dataset3, y)

dataset3$sumF <- dataset3$beF + dataset3$bpF
dataset3$sumR <- dataset3$beR + dataset3$bpR + dataset3$weR
dataset3$sumFR <- dataset3$sumF + dataset3$sumR
View(dataset3)

#ANOVAS
anova_pair_F <- aov(NrmzMeanConfPair_name ~ sumF, data = dataset3)
summary(anova_pair_F)
anova_pair_R <- aov(NrmzMeanConfPair_name ~ sumR, data = dataset3)
summary(anova_pair_R)
anova_pair_FR <- aov(NrmzMeanConfPair_name ~ sumFR, data = dataset3)
summary(anova_pair_FR)

anova_event_F <- aov(NrmzMeanConfEvent_name ~ sumF, data = dataset3)
summary(anova_event_F)
anova_event_R <- aov(NrmzMeanConfEvent_name ~ sumR, data = dataset3)
summary(anova_event_R)
anova_event_FR <- aov(NrmzMeanConfEvent_name ~ sumFR, data = dataset3)
summary(anova_event_FR)

anova_detail_F <- aov(NrmzMeanConfDetail_name ~ sumF, data = dataset3)
summary(anova_detail_F)
anova_detail_R <- aov(NrmzMeanConfDetail_name ~ sumR, data = dataset3)
summary(anova_detail_R)
anova_detail_FR <- aov(NrmzMeanConfDetail_name ~ sumFR, data = dataset3)
summary(anova_detail_FR)

#AVERAGE FIXATION DURATION AND SACCADE AMPLITUDES
dataset$duration = as.numeric(dataset$duration)
dataset$sac_amplitude = as.numeric(dataset$sac_amplitude)
dataset$duration2 <- (dataset$duration)*(1000/256)
dataset4 = dataset %>%
  filter(Refi != "[]")
View(dataset4)

tapply(dataset4$duration2, dataset4$Refi, summary, simplify = T)
tapply(dataset4$sac_amplitude, dataset4$Refi, summary, simplify = T)

anova_dur <- aov(duration2 ~ Refi, data = dataset4)
summary(anova_dur)
anova_sac <- aov(sac_amplitude ~ Refi, data = dataset4)
summary(anova_sac)

tukey_dur <- TukeyHSD(anova_dur)
tukey_dur
tukey_sac <- TukeyHSD(anova_sac)
tukey_sac

lm_dur <- lm(duration2 ~ Refi, data = dataset4)
summary(lm_dur)
lm_sac <- lm(sac_amplitude ~ Refi, data = dataset4)
summary(lm_sac)
