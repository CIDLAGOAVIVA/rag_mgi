## Estimating  and  Forecasting  the  Volatility  of Brazilian  Fi­ nance  Series Using  ARCH  Models'

J  oao  Victor Issler"

## Abstract

The goal  of this paper is to  present  a comprehensive emprical  analysis  of the return and conditional variance of four Brazilian financial series using models of  the A  RCH class. Selected  models  are then compared regarding  forecasting accuracy  and  goodness-of-fit  statistics. To  help  understanding  the  empirical results,  a self-contained theoretical discussion of ARCH models is also presented in  such  a  way  that  it  is  useful  for  the  applied  researcher. Empirical  results show  that  although  all  series  share ARCH and  are leptokurtic  relative  to  the Normal, the return on the US$ has clearly regime switchlng and no asymmetry for  the  variance,  the  return  on  COCOA  has  nO asymmetry,  while  the returns on the Cbond and Telebras have clear signs of asymmetry favoring the leverage effect.  Regarding forecasting,  the  best  model  overall  was  the EGARCH(l,l) in its  Gaussian version.  Regarding goodness-of-fit  statistics,  the SWARCH model did  well,  followed closely by the Student-t GARCH(l,l).

## Resumo

Esse artigo apresenta uma analise emp f rica abrangente da variancia condi� cional do retorno de quatro ativos comumente trasacionados  pelos mercados fiw nanceiros brasileiros usanda varios modelos da classe ARCH. Esses modelos sao posteriormente  comparados  relativamente a sUas  capacidades  preditivas  e  es­ tat i sticas de aderencia.  Precedendo a analise emp i rica discute-se, em uma segao autocontida,  as  propriedades  de modelos ARCH de uma forma que seja uti!  a urn  econometrista aplicado  tentando  modelar  series brasileiras. as  resultados

Estimating and Forecasting the Volatility of Brazilian Finance Series mostram  que  as  propriedades  das variancias  das  diferentes  series  sao  distintas. Embora todas as distribui�6es condicionais possuam caudas pesadas, a volatili­ dade do cambia tern mudanc;as de regime, a da serie de CACAU nao tern assime­ tria na variancia, enquanto os rerernos de Telebras e do Cband mostrem sinais de assimetria na variancia favorecendo 0 "efeito alavancagem".  Com relac;ao a pre­ visDes um-passo-a-frente, 0 melhor modelo foi 0 EGARGH(l,l} Gaussiano.  Com rela,ao as estat sticas de aderencia, i 0 melhor modelo doi 0 SWARGH, seguido de perto pelo modelo GARGH(l,l} com distribuiqao t de Student.

Key Words: ARCH models;  volatility;  Brazilian financial series;  emerging  mar­ kets.

JEL Code: C22 and G12.

## 1.  Introduction

ARCH - Autoregressive Conditional Heteroskedasticity - is rec­ ognized  today  as  a  major  feature  of  financial  data  which  several econometric models try to capture.  This paper presents  a compre­ hensive empirical analysis of the return and conditional variance of a variety of Brazilian financial series using models of the ARCH class. The  data used  covers  a  wide spectrum  of Brazilian Finance  series: a  spot stock-price index - IBOVESPA, of the Sao Paulo Stock Ex­ change, the spot price of a popular Brazilian stock - Telebras, traded in  the Sao  Paulo Stock Exchange,  a spot currency-exchange  rate R$/US$,  and a spot popular commodity price - COCOA.  Selected models of the ARCH class for the return of these series are fitted and estimates compared regarding forecasting accuracy and goodness-of­ fit statistics.  To  help understanding the empirical results obtained, a self-contained theoretical discussion of ARCH models is also pre­ sented,  focusing  on econometric results of  ARCH  models  that  are useful for the applied researcher.

## Joao Victor Issler

Empirical results show that all series  share ARCH and are lep­ tokurtic relative to the Normal.  However, they all have specificities as well:  the return  on  the US$ has regime switching and no asym­ metry  for the variance, the return on COCOA has no asymmetry, while  the  returns  on  the  Cbond and Telebras  have signs  of  asym­ metry favoring the leverage effect.  This stresses the point that suc­ cessful  modelling  of  asset  returns  requires  taking into account  the essential features of each of them separately.  Regarding forecasting accuracy, the best model overall was the EGARCH(l, 1) in its Gaus­ sian version.  This may  be due to the fact that,  for Brazilian data, outliers are a common occurrence.  Regarding goodness-of-fit statis­ tics, the SW ARCH model did well, followed closely by the Student-t GARCH{1, l).

## 2.  Some Theory of ARCH Models

In this section selected results for ARCH models are presented. Since the literature on ARCH is vast and comprehensive, including more than one hundred papers and the surveys of Bollerslev,  Chou and Kroner  (1992), of Bollerslev,  Engle and Nelson  (1994), and the book of collected papers edited by Engle (1995), it makes little sense to repeat here theoretical results that are already discussed elsewhere at greater depth and length.

Instead,  the  focus  of  this  section  is  on  econometric  results  of ARCH models that are useful for the applied researcher.  In a direct analogy  with the time-series  method proposed by  Box and Jenkins (1976), the  "identification" of ARCH processes is motivated here by considering autocorrelation and partial autocorrelation functions for the squared ( returns of financial ) series.  We later discuss three im­ provements for the class of ARCH models: the generalized ARCH GARCH, the Exponential GARCH - EGARCH, and the switching­ regime  ARCH  model - SW ARCH,  motivating their  introduction

Estimating and Forecasting the Volatility of Brazilian Finance Series by  previous  shortcomings  in  applying  early  ARCH  models  to  ac­ tual (Finance) data.  All models discussed here are later applied to Brazilian financial data.

## 2.1.  ARCH:  the  basic  idea  and  selected models

Time series {Yt}r;l have two basic  properties  that made mod­ elling and forecasting them easy to a wide audience; see Box e Jenk­ ins  (1976)  and  all  the  literature  that  follows. The  first  is  weak stationarity,  which  imposes the restriction that E[Yt] = J.L, Vt,  and E[(Yt-/l)(Yt-j-J.L)] = "tj, Vt,j. These restrictions may apply to the original series {Yi}r;l or to some transformation of it  (e.g.,  its first differences).  Since time only goes forward, the econometrician has to form time averages to estimate consistently  population parameters of  time-series models.  Thus,  without this property, it  would be im­ possible to conceive consistent estimates due to the lack of degrees of freedom.  The  second  property  is autocorrelation, i.e., the  fact  that it is usually  the case that "tj # 0 for some j &gt; O. Again,  this  prop­ erty  may  apply  to  the original series {Yt}r;l or to a transformation of it  (e.g.,  its square).  Autocorrelation allows modelling time series based on their own  "past",  and on  an unpredictable error ( €t ) and its own "past".  Thus, forecasts will be a function of current and past values of Yi and €t. In models popularized by Box and Jenkins,  the functional form is linear,  but there are several examples of models that use a non-linear  function.  Perhaps, the most important one in Finance is the class of ARCH models introduced by Engle (1982).

Although the ARCH model and its  extensions  are  widely  ap­ plied in Finance today,  that  was not at  all its original motivation. Engle  (1995,  pp.  xi-xii)  writes that he thought that  the main con­ tribution of ARCH models would be on the Rational Expectations debate  in Macroeconometrics. By the  end of  the  1970's,  inflation was soaring everywhere due to two oil shocks.  This raised concerns

of how well it could be forecast.  Indeed,  Okun ( 1971 ) and Friedman ( 1977 ) proposed that an increase in the level of inflation would raise its variance.  Interestingly enough,  using the framework of his 1982 Econometrica paper, Engle ( 1983 ) showed that the high level of US inflation experienced around that  time was highly predictable,  and that inflation level and variance were uncorrelated.

As is the case with several successful theoretical developments in econometrics, Clive Granger reports that the birth of ARCH mod­ els  was  a  consequence  of  an  observed  empirical  regularity. When applying the tools proposed by Box and Jenkins, one could find se­ ries  which  were  unpredictable,  although  their  squares  were  highly predictable. This suggested that some sort of non-linearity  was at work.  This  lead Engle ( 1982 ) to propose the class of ARCH mod­ els,  which  conforms to this  early  empirical  observation. Granger, on the other hand, went on to work with the bilinear model,  which has a structure similar to  that of ARCH models;  see Granger and Andersen 1978 . ( )

The linear  ARCH(P)  model introduced by Engle  can be  sum­ marized in:

<!-- formula-not-decoded -->

where D(.) is  some parametric distribution,  usually the  Normal or the Student-t, and Xt is either weakly exogenous or an element of the conditioning set nt-I. Notice the similarity between the last line in ( 1 ) and an AR(p) model:

<!-- formula-not-decoded -->

Estimating and Forecasting the Volatility of Brazilian Finance Series

It  is  easy  to  write  an  ARCH  process (1) as  an  autoregressive process (2), using  the  result  that el = E [ell n t -d +  Tit, where {1) t}t� l is a Martingale-Difference  Sequence.  We have:

<!-- formula-not-decoded -->

To ensure that et 2: 0, Vt, for  all possible realizations of {edt;:;l' it is  usually  assumed that  (i) no &gt; ° and ni 2: 0, Vi = 1, ...  ,p, and that (ii) 1) t has a lower bound of -no.

The  simplest  linear  ARCH  model  possible  the  Gaussian ARCH(I), with fJ = 0,  allows discussing several interesting features of models in this class.  It is summarized in:

<!-- formula-not-decoded -->

Notice that if n1 = 0, Yt  I nt -1 � N(O, no), i.e., Yt is  conditionally homocedastic. The theorem below shows some of its basic properties.

Theorem 1. (Engle (1982)).  F or integer r, the 2rth (unconditional) moment of a first-order linear ARCH process  with no &gt; 0, n1  2:  ° exists  if,  and only i f , n'iIIj=l (2j - 1) &lt; 1.

Thus, the second and fourth unconditional moments are defined, with E(Y?) =  1 �� " and E(Y/) = ( 1 3:�)2 . /�3�;' iff n 1 &lt; 1 and 3nr &lt; 1 respectively.  This has two implications.  First, although the conditional model is Gaussian, the unconditional distribution has fatter tails compared to the Normal. I This happens because L�·3':,t &gt; 1. I

Under a Gaussian unconditional distribution, the Kurtosis coefficient 2 3 2 1 2 . . b  y 3  ( a Q h  ence  sma  er  th  an II a o � S  econd  , IS given l -a,) 2  , ( 1 a,l" . 1-3a�' although the conditional distribution is heteroskedastic,  the uncon­ ditional distribution is homocedastic.  Indeed, because the mean and autocovariances of Yi are not time varying, this process is weakly sta­ tionary despite displaying conditional heteroskedasticity.  This result generalizes for a wider  class of ARCH(P) models as below.

Theorem  2. (Engle (1982)).  The pth-order linear ARCH process with aD &gt; 0, a1," ', a p �  0 is  covariance(weakly-)  stationary i f , and only if,  the associated characteristic equation has  all roots  out­ side the unit circle. The stationary variance is given by 1 r;'f�, a,'

This last result illustrates why the appropriate ARCH(p) model conforms  to the  stylized  fact that the level series  (error)  is  white noise  despite  the  fact  that  the  autocorrelation  and  partial  auto­ correlation  of  its  squares  show  signs  of  predictability. Following Bollerslev (1986), write the error term in (3) as ct = O"t · Zb where Zt � i.i.d.(O, 1). Based on the  law of iterated expectations is easy to  show that E[ct] = 0, E[ctct\_ j] = 0, Vj &gt; 0, and given Theorem 2, E[c�] = 1 B't , a,' Hence, ct is  white noise.  However,  if we take cF = O"t . z;, it is  obvious that its  auto  correlations  will not die  out because of (3), and that its partial autocorrelation will only be zero starting at order p + l.

Estimating  an ARCH(p) process  by  maximum  likelihood  is straightforward once a parametric distribution is assumed for Zt in Ct = O"t  .  Zt. The usual assumption is that Zt has an i.i . d. Gaussian or Student-t distribution.  In any case,  the joint density of the sam­ ple Yl," ', YT can  be  recursively  factored into the  conditional  and

marginal densities to form:

<!-- formula-not-decoded -->

where 9 is a vector of  parameters of  the joint density, and we con­ dition on pre-sample observations.  For the simple ARCH(l) model discussed above we have:

<!-- formula-not-decoded -->

where 9  = (ao,  all'. Using this  result,  maximum likelihood  esti­ mates  can be found by numerically  optimizing the  conditional log­ likelihood function:

<!-- formula-not-decoded -->

subject  to the constraints ao &gt; 0 and a1 :::: o.

For  Financial series,  if  one  believes  that  outliers  are  clustered (e.g.,  Mandelbrot (1963)), then  the  estimation  method  described above reduces the impact of these extreme observations on parameter estimates.  This happens because the denominator ofyf jao + a1  Y'f-1 will  reduce  the contribution  of  a given  outlier Yt in  (7),  since Yf -1 is  more  likely to be large  as  well.  This  shows  a  clear  advantage  for recognizing the presence of ARCH when compared to (say)  the case

## Joiio Victor Issler

where homocedasticity is erroneously assumed.  In the latter, all ob­ servations are equally weighted in the likelihood function, whereas in the former outliers get a smaller weight.  Coupled with the fact that the unconditional distribution is leptokurtic relative to the Normal, allowed Engle (1982) to  conclude  that ARCH models show poten­ tial to deal with clustered outliers.  Of course, if outliers are not clus­ tered, the weighting procedure will not work.  Hence, Engle mentions nothing regarding outliers in general.  He also makes no attempt to compare ARCH models with  "robust" estimates.'

From empirical experimentation  with models in the ARCH(P) class,  it  became  apparent  that  the  order  of  the  fitted  model  was quite large - p large.  In a direct analogy  with models in the AR(p) class,  where the  parsimonious solution is to include M  A(-) terms forming an ARMA model,  the ARCH(P) process  was  generalized to include these "M  A( q) terms".  This is the motivation behind the GARCH(p, q) model, proposed by Bollerslev (1986):3

<!-- formula-not-decoded -->

where A(L) = E;=I  QiLi and B(L) = Ef =I (3iLi are  finite  order polynomials on the lag operator L. To see how the solution proposed by  Bollerslev  mimics  the ARM  A class,  consider  for  simplicity  the GARCH(l, 1) model:

<!-- formula-not-decoded -->

Estimating and Forecasting the Volatility of Brazilian Finance Series

If  we define as in (3), 11t = c�  a} as the conditional variance  pre­ diction error,  with the property that E[ 11 t I nt-1] = 0, we can solve (9) in terms of current and lagged lOt and 11t to get:

<!-- formula-not-decoded -->

which  is  an  ARM  A(I, 1) process  for lO r . Using  the  same  princi­ ple, it  is  easy  to  show  that  a  GtRCH(p, q)  model  is  indeed  an ARMA(max(p, q), p) for c�; see Bollerslev (1986).

The Theorem below shows that the result in Theorem 2 gener­ alizes for this wider class of ARCH models.

Theorem  3. (Bollerslev (1986)).  The  Gaussian GtRCH(p, q)  p r o ­ cess,  with w &gt; 0, o;i,  (3 i � 0, Vi = 1,  . . . , max[p, q ] ,  is  weakly station­ an)  with E(ct) = 0, Var(ct) = (1 A( l ) B ( l )) and C o v ( ct , lOs) = 0, tis, if,  and only  if, A(I) + B(I) &lt; 1.

The analogy between the ARM  A and the GtRC  H class is also present  when  forecasting  is  considered,  because  the  GtRCH(p, q) model is linear on lagged lO t and er r . For  the  GtRCH(I, I)  model, defining Eter;+s = E[er;+s Int] as the forecast of the conditional vari­ ance for horizon s, using information up to t, we have:

<!-- formula-not-decoded -->

Taking the conditional expectation of the last line of (11) using the conditioning set nt. it is easy  to show using  the law of  iterated ex­ pectations that:

<!-- formula-not-decoded -->

## J  oao Victor Issler

As long as the parameter-restriction and stationarity conditions in Theorem 3 hold,  Le., 0 &lt; a + i3 &lt; 1, the expression in (12) con­ verges to the unconditional variance of et as the forecasting horizon increases:

<!-- formula-not-decoded -->

The Exponential G4RCH - EG4RCH model was proposed by Nelson (1991) to deal with three basic shortcomings of models in the G4RCH class.'  First, the impact of shocks on volatility is symmetric for these models.  Hence, positive or negative shocks have exactly the same effect on the conditional variance.  Since most applications of models in the G4RC  H class are in Finance, and for these data it is observed that the effects of positive and negative returns on volatil­ ity  is not  identical ( e.g.,  Black (1976)), it  is  desirable  to  conceive models that  allow  estimation  and  testing  for  asymmetry. Second, the  restrictions ao &gt; 0, ai,  i3i :::: 0, Vi,  constrain  the  roots  of  the characteristic  polynomials  of  G4RCH  models,  preventing  random oscillatory  behavior  in of Moreover,  when  these  restrictions  are binding,  maximum  likelihood  estimates  are  a  constrained  optima. Third, measures of persistence of shocks to the conditional variance for  integrated  G4RCH  processes  depend  on  the  norm  considered, and  no  direct  analogy  can  be  made  with  results  of  the  unit-root Iiterature.5

We consider here a simpler version of the EG4RCH model pro­ posed by Nelson:

<!-- formula-not-decoded -->

The  third line in  (14)  allows  for  asymmetric  effects  of  shocks on  the  (log  of  the)  conditional  variance. When Zt &gt; 0, the  slope of g(Zt) is  B + " but  for Zt  &lt; 0, the  slope  of g(Zt) is B -,. The fourth line depicts a simple ARM  A process for In(ul),  proposed by Nelson as a parsimonious representation for the infinite M  A process for  In(uD. In  his  original  formulation,  he  also  considered  a  time varying intercept for In(ul).

Theorem  4. (light  version  of  Nelson  (1991)). I f at  least  one  of the parameters,  or B are non-zero, {exp( -w  u ) n , {exp( -w /2)ct}, and { In (u r ) - w } are strictly  (strongly)  stationary and ergodic,  and {In( u l ) -w } is  covariance-stationary if,  and only if, 2:: : 1  f31 &lt; 00.

It is worth noting that the ARM  A specification presented above is  widely  used  in applications,  being  the  most relevant  for  the  ap­ plied researcher.  In this case, a necessary and sufficient condition for 2:: :1 f3 1 &lt; 00 is that all the roots of  (1 - rP1Z - ...  - rP p z P ) = 0 lie outside the unit circle.

For the EG1RCH(I, 1) model, the (log) variance equation is:

<!-- formula-not-decoded -->

## Joao Victor Issler

where  the  model has  been reparameterized  with w' = (1 -¢r)w -'YEl zt - ll, and fJ = ¢l. A slightly different specification is considered in Hamilton (1994, pp. 668-669):

<!-- formula-not-decoded -->

In either (15) or (16) there is no asymmetry in the variance as long as 'Y = O. This constitutes a  testing procedure  for the asymmetric effect. If 'Y  f=  0, then  there  is  a  differentiated  impact  of  news  on volatility. If ' Y  &lt;  0 there is the so  called  "leverage  effect,"  where good news have a smaller impact on the conditional variance than bad news; see Pagan and Schwert (1990) and Engle and Ng (1991).

Another model that allows estimating and  testing the  leverage effect  is  the  Threshold ARCH T ARCH model,  proposed  inde­ pendently by Zakoian (1990), and Glosten, Jaganathan, and Runkle (1993). The specification for the conditional variance is:

<!-- formula-not-decoded -->

where  the  dummy  variable dt-l = 1, if Ct\_l  ::;  0, and dt-l = 0 otherwise.  Again,  there is no asymmetry in the variance as long as 'Y = O. Here, there is the leverage effect if'Y &gt; O.

At  least  since  Bollerslev (1986), there  was  a  switch  in  focus from  Macroeconometrics to Finance  for models  within the ARCH class.  By the time Nelson proposes the EGARCH model, this change is  already  consolidated. Later,  the  work  of Hamilton  and  Susmel (1994) on ARCH and switching-regime models is motivated by the fact that "financial markets sometimes appear quite calm and other times highly volatile". According to Diebold (1986) and Lamoureux and Lastrapes (1990), one of  the consequences  of ignoring possible changes in regime is an overestimation of the persistence of shocks to the conditional variance.  Hamilton and Susmel note that this relates

Estimating and Forecasting the Volatility of Brazilian Finance Series

"to Perron's (1989) observation that changes in regime may give the spurious impression of unit roots"  .

Nowhere  there  are  more  changes  in  rules  and  is  volatility  so high  than  in  emerging-market  economies. Because  this  feature  of emerging-market financial data leads to potentially  interesting  ap­ plications of techniques that recognize changes in regime, we discuss now the switching ARCH - SWARCH model of Hamilton and Sus­ mel.  The SWARCH -L(k, q) model, where the L stands for leverage ( or asymmetric effect , ) k denotes the number of regimes, and q de­ notes the order of the ARCH process, is given by:

<!-- formula-not-decoded -->

where dt - l = 1, if Ut-l :::; 0, and dt-1 = 0, if Ut - l &gt; 0 is the dummy variable  for  the  leverage  effect,  and St represents  all the  possible regimes for the variance process.  For regime one,  Le., when St = 1, the variance factor is normalized to unity, Le., 9 1 = 1. When St = 2, all things  equal,  the variance of Ut is 92 times higher than that in regime one, and so on, up to 9k, where St = k.

As in the rest of the literature on ARCH, it is usually assumed that Zt is either Gaussian of has a Student-t distribution. It is further assumed that St can be described by a Markov chain.  The probability that there  is a change in regime on t,  going from regime i in t -1, to regime j, is:

<!-- formula-not-decoded -->

where it is useful to collect all these parameters in a transition prob­ ability  matrix, P=(Pij) , of  order k x k. Notice that 'E =1 � Pij = 1. Hence,  the columns of P add up to unity.  Along with the variance

## J  DaD Victor Issler

factors gl, g2," ',  gk, these  probabilities  are  additional  parameters to  be estimated.  In forming the likelihood function, it is recognized that observations may come from any of these states, and thus prob­ abilities are used as weights; see Hamilton and Susmel for details.

## 2.2.  Estimation,  inf erence  and  testing

It  is  common  practice  to  estimate the  models  discussed  above by  maximum likelihood after  a  parametric distribution  for  the  er­ ror  term  is  assumed. For  applied  research,  since  there  is  usually doubt  about  which  parametric  distribution  to  use,  it  is  helpful  to regard  these  estimates  as  quasi-maximum likelihood;  see Bollerslev and Wooldridge (1992) inter-alia. There is also the possibility of es­ timating ARCH processes by non-parametric, semi-parametric and semi-non-parametric methods; see Engle and Gonzalez-Rivera (1991) for  semi-parametric methods,  Hamilton (1994) for  a  discussion  on non-parametric estimates of ARCH processes using the generalized method of moments (GMM), and Gallant and Tauchen (1989) and Gallant et al. (1991, 1992, 1993) for semi-non-parametric methods.

To perform conditional maximum likelihood estimation, first de­ compose the joint density of the sample WI, . · · , WT recursively as a prod  uct of conditional densities to form:

<!-- formula-not-decoded -->

where 9 is a vector of parameters of the joint density, Wt is a vector that  includes  the  explained  and  explanatory  variables,  and  condi­ tioning on pre-sample observations up to -k is implicit.

There are several examples of parametric densities that are used in practice  in forming (20). Bollerslev (1986) assumes  conditional

normality  for  the  error  term lOt of  the G!RCH(p, q) model  in (8), i.e.:

<!-- formula-not-decoded -->

whereas Bollerslev (198 7 ) assumes that lOt has a Sudent-t distribution with v degrees of  freedom and scale parameter Mt (to  yield  a  unit variance).  Hence,

<!-- formula-not-decoded -->

where r[.] is the gamma function.

The density in (22) allows for fatter tails than the one in (21). The parameter v controls how fat the tails are.  Since the Normal can be thought as a limiting case of the Student-t density  when v --+  00, using (22) in place of (21) allows  the estimation procedure to select the  number of  degrees  of  freedom that best  fits the data,  thus  not ruling  out  leptokurtosis a priori. If  the  estimate  of v is  relatively large, then the Normal may not be a bad approximation.

Because the  Sudent-t distribution,  with v finite,  may  imply  no finite  unconditional  moments  for  the  error  process,  Nelson (1991) proposes  the use  of  the  Generalized  Error  Distribution  (GED). Its density function, for a random variable normalized to have zero mean and unit variance,  is:

<!-- formula-not-decoded -->

where &gt;-= [ 2 (-2 / v ) r[l/v] r[3/VJP/ 2 . As in the  Student-t density, v controls the tickness of the distribution tail.  For v = 2, the density

(23) collapses to the Standard Normal, a result that can be used for a Normality test.  For v &lt; 2, it has ticker tails than the Normal and vice-versa for v  &gt; 2. For v = 00,  z is uniformly distributed on the interval [ \_3 1/2 ,3 1/2 ] .

With correct specification for the functional form of f(Wt IWt-l, ...  , W-k ; (J),  the  log-likelihood  function  can  be  written as:

<!-- formula-not-decoded -->

where It 0 is  the  individual  likelihood  contribution. The  function (24) is  usually  maximized  by  numerical  methods  subject  to  non­ negativity  constraints  whenever  necessary. If  (Jo  is  the  true  value of  the  parameters  in (24), where (Jo E int e, and e is  a  compact subspace of a Euclidean space such that the error process has finite second moments,  then,  under fairly  general conditions ( e.g.,  Weiss (1986)), the  maximum  likelihood  estimate  of  (J, OT, converges  in distribution as  follows:

<!-- formula-not-decoded -->

where leI = [-E( 8;;��1 I nt\_1)t 1 is the inverse  of  Fisher's Infor­ mation Matrix.  Un 'iI er a correctly specified model, the latter can be consistently estimated by (T -1  'L,[ = 1 8;b') 8��;) ) -1 , evaluated at OT, allowing inference on (J to be conducted using (25),

If  there  is  doubt  about  the  parametric  density f  (Wt  I  Wt-l, "',  W\_k; (J ) , but the researcher uses the Normal density, OT can stilI

Estimating and Forecasting the Volatility of Brazilian Finance Series be regarded as the quasi-maximum likelihood estimate of (J. In this case,  inference  can  be  conducted  using  the  appropriate  correction proposed by Bollerslev and Wooldridge (1992), which relies on:

<!-- formula-not-decoded -->

where S \_ plim (T -1 "T 81,(·) al,o)  , and D \_ plim L..t=1 {j(J"" a (J 1 (T -1 Lf=1 \_ E(a 2�� .) O(J' I  nt-I)), for  which  consistent  estimates can also be constructed making inference feasible.

Testing for ARCH can be easily performed via a Lagrange Mul­ tiplier type test proposed by Engle (1982) using the following steps:"

- 1. Run an ordinary least-squares regression to get the residuals ft. Square them to get Ef.
- 2. Regress Ef on a constant and m of  its  own  lags,  obtaining R� -the uncentered R-squared statistic of this last regression.
- 3 . Under the null that ct � i.i. d.N(O, a2 , ) T .  R� � X;;'. Thus, by comparing T·  R� with the appropriate entry of ax2 distribution table,  one can test the null of no ARCH.

## 3.  Volatility  in Finance

Volatility  is  the  generic  name  for  conditional  standard  devia­ tion.  In Finance, the term is usually employed to denote the condi­ tional standard deviation of asset returns. Although this subject has evolved considerably in the last twenty years,  the market-volatility measures that have been employed in practice are  quite naive in  a statistical  sense,  since the heteroskedasticity  present  in  market  re­ turns is not usually recognized.  Denoting by T t the demeaned return

of a given asset, it is not uncommon for  traders  to use the following statistic to measure asset-return volatility:

<!-- formula-not-decoded -->

Notice  that ( ) i V;2  is  the  maximum  likelihood estimate  of  the variance  of  the  return  only  if rt is  homocedastic and  normally  dis­ tributed,  and ( ii ) VI is  calculated  using  a  fixed  window  of N ob­ servations.  Using a  window with width N generates an unpleasant property  for VI: there  is  a ( an almost ) discrete  jump  for  it  when an extreme rt observation  is  either  included  or  excluded  from  the average in (27).

A second commonly used device is the exponential smoothing St for the squared asset return:

<!-- formula-not-decoded -->

where A is the decay  parameter used to smooth-out lagged squared returns, and it is assumed that 0 &lt; A &lt; 1. This procedure is identical to the use of a convex combination of lagged St and current r;, as shown  in  the  last  line  of (28). Using VS; as  a  volatility  measure makes the impact of outliers on VS; to decrease as time passes, thus it looks smoother than VI.

A third commonly employed volatility measure is the  "implicit volatility"  derived  from  solving  the  Black  and Scholes (1973) for­ mula.  A usual problem for this measure is the implicit assumption

Estimating and Forecasting the Volatility  of Brazilian Finance Series of log-Normality for the asset price,  despite overwhelming empirical evidence to the contrary.

All volatility measures  described  above disregard the het­ eroskedasticity  present  in  asset  returns'  and  the  autocorrelation structure of squared returns.  Put in simple terms, they may throw out  important information about current an future volatility.  Here we  go  back  full  circle  to  Engle's (1982) original  idea  on  Rational Expectations:  if there is information on the conditional variance of returns,  why not use it?

Models of the ARCH class recognize from the outset that het­ eroskedasticity  is  an  empirical  regularity  of  financial  data. They incorporate this feature of the data by using a simple and ingenious time-series mode!.s In  an interesting  study,  Noh,  Engle  and Kane (1994) suggest the  use  of (Jt = VE[E:� I nt - I] ( where E:t is  the  in­ novation in  the return series ) as  a measure of  volatility  for  the re­ turn of  the  S&amp;P500  index. Indeed,  these  authors  find  that profits using  G4RCH I, I -volatility forecasts significantly  exceed transac­ ( ) tion  costs  for  near-the-money  straddles.  This shows  that although ARCH has a second order effect on forecasting returns, money could be made by using such information.

G4RCH-volatility  forecasts  have  several  interesting  features. For a stationary  G4RCH I, ( 1) model, (13) and (12) above show re­ spectively that variance forecasts ( i ) have mean reversion to the un­ conditional variance,  and ( ii ) use the most recent information with the appropriate weights to forecast the variance into the future.  Re­ garding  the  latter  there  is  a  similarity  between  G4RCH-volatility

forecasts and  the  use of  the exponential smoothing device.  Starting with ( 9 ,  and  assuming that ) a, f3 &gt; 0 and 0 &lt;  a + f3 &lt; 1,  we  can solve for al in terms of the lagged squared errors to get:

<!-- formula-not-decoded -->

which  shows  that  the  GlRCH  model  is  a  way  of  exponentially smoothing  past return  innovations;  see ( 28 ) above. Indeed,  if ( de­ meaned ) returns are unforecastable, ( 29 ) will be a weighted average of lagged squared returns  with exponentially decreasing weights.

## 4. Estimating  and  Forecasting  Volatility  in  Brazilian  Fi­ nance  Series

## 4.1.  The  data

The data used covers a wide spectrum of Brazilian Finance se­ ries:  a spot stock-price index - IBOVESPA, of the Sao Paulo Stock Exchange,  the  spot  price  of  a  popular  Brazilian  stock Telebras, traded in the Sao Paulo Stock Exchange,  a spot currency-exchange rate - R$ / US$, and a spot popular commodity price - COCOA, with data extracted from the ICCO database.  All asset-prices are US$ de­ nominated and data frequency  is daily ( except for  weekends . ) For the COCOA series the sample covers the period from January 5th, 1990  through July  1st,  1998.  For the R$ / US$ and Telebras series the sample covers the period from July 4th, 1994 through July 1st, 1998.  For the Cbond series the sample period goes from July 18th, 1994 through July 1st, 1998.

There  are  some missing  values  for  all series. Most are  due  to holidays.  To keep the data frequency uniform across the sample  ex­ ( cluding weekends , missing observations  were  completed using the ) most  recent  quote  for each series. Using the  transformed  data set,

the  percentage  instantaneous  return  for  each  series  was  calculated using  a  log-difference  transformation,  i.e.,  for  each  price  series Zt, 100 x Aln zt ( ) was  computed. Plots  of  the  data  are  presented  in Figure 1. As is typical of financial series,  they  all show sign of het­ eroskedasticity and volatility clustering.

<!-- image -->

F i9 u re  1 Return of BraZilian  Finance  Series

<!-- image -->

-eBON

<!-- image -->

<!-- image -->

The return of the US$ shows two distinct patterns of variation during the sample  period,  reflecting the change in regime from the wide  target  zones  of  the  beginning  of  the  Real  plan  to  the  narrow target  zones  implemented  after  the  floating  of  the  Mexican  Peso. With the exception of the COCOA series,  which is  traded abroad, all  series  traded  in  Brazil  vary  wildly  in  relative  terms  during  the Mexican and the Asian crises.

## 4.2.  Estimation results

Autocorrelation and partial autocorrelation functions for all re­ turns and their squares,  as well as other basic statistics for the data, are  presented  in  table  1. A  utocorrelation  coefficients  are  rather small,  reflecting  no obvious predictability. Indeed,  if returns  were predictable,  there would be arbitrage opportunities for  the  average investor. Since anyone can be an average investor,  there can be no autocorrelation for the return."  The  highest estimate  for the auto­ correlation coefficient is 0.12. It happens for the return on the US$ at lag five.  Compared to the benchmark of 2/ VT = 2/v'1039 c:: 0.06, it is  significant. However,  the  use  of this  benchmark  is  only  valid under homocedasticity.  Indeed,  the benchmark underestimates the approximate 95% confidence interval if the data is heteroskedastic, which is probably the case.lO

The autocorrelation coefficients for squared returns show a com­ pletely different pattern, reflecting the fact that the conditional vari­ ance of returns is predictable.  This is corroborated by the fact that all  ARCH  tests  performed  reject homocedasticity  of  returns  with great confidence.  Also,  the Jarque and Bera  (1987)  normality  test rejects Normal returns for all series.  The latter has little to do with returns having a skewed distribution, being basically a consequence of  outliers  in  these series;  see  the  very  high  Kurtosis  coefficient  for all of them in table 1a.

## Estimating and  Forecasting the Volatility of Brazilian Finance Series

## a) Descriptive Statistics

|                                   | US$    | CBOND   | COCOA   | TELEBRAS   |
|-----------------------------------|--------|---------|---------|------------|
| Mean Daily Return  (%)            | 0.023  | 0.067   | 0.032   | 0.114      |
| Skewness                          | 0.181  | -0.545  | 0.405   | 0.685      |
| Kurtosis                          | 18.641 | 17.727  | 9.483   | 15.741     |
| Jarque-Bera Test  P-value ( )     | 0.000  | 0.000   | 0.000   | 0.000      |
| Unconditional standard  deviation | 0.282  | 1.875   | 1.633   | 3.227      |
| ARCH 5) Test  P-value)  ( (       | 0.000  | 0.000   | 0.000   | 0.000      |
| AR l) Robust t-test  ( ( P-value) | 0.006  | 0.928   | 0.200   | 0.990      |
| Number of Observations            | 1,039  | 1,094   | 2,210   | 1,039      |

AR{l) coefficient  standard  error calculated using the procedure in Newey  and West  (1987).

## b ) Autocorrelation  and  Partial  Autocorrelation  Functions  of Returns  and  Squared Returns

| Returns   | US$              | CBOND            | COCOA           | TELEBRAS         |
|-----------|------------------|------------------|-----------------|------------------|
| PI(al)    | 0.106 (0.106)    | -0.007 (-0.007)  | -0.039 (-0.039) | -0.002  (-0.002) |
| pz(az)    | -0.012  (-0.023) | 0.017 (0.017)    | -0.042 (-0.044) | -0.030 (-0.030)  |
| P3(a3)    | -0.082  (-0.079) | -0.107 (-0.107)  | -0.007 (-0.010) | -0.042 (-0.042)  |
| P4(a4)    | 0.037 (0.055)    | -0.013  (-0.015) | 0.013 (0.011)   | -0.025  (-0.026) |
| ps(as)    | 0.120 (0.110)    | -0.037 (-0.035)  | -0.010 (-0.010) | -0.080 (-0.083)  |
| 2/VT      | 0.062            | 0.060            | 0.043           | 0.062            |

| Squared  Returns   | US$            | CBOND          | COCOA           | TELEBRAS       |
|--------------------|----------------|----------------|-----------------|----------------|
| PI  (all           | 0.234 ( 0.234) | 0.271 ( 0.271) | 0.123 ( 0.123)  | 0.145 ( 0.145) |
| pz(az)             | 0.157 ( 0.108) | 0.287 ( 0.230) | 0.042  ( 0.027) | 0.217 (0.200)  |
| P3(a3)             | 0.160 ( 0.109) | 0.234 ( 0.128) | 0.D28 ( 0.020)  | 0.154 ( 0.106) |
| P4(a4)             | 0.160 ( 0.097) | 0.060 (-0.087) | 0.017 ( 0.010)  | 0.084 ( 0.014) |
| ps(as)             | 0.162 ( 0.091) | 0.074 (-0.008) | 0.058  ( 0.055) | 0.105 ( 0.047) |
| 2/VT               | 0.062          | 0.060          | 0.043           | 0.062          |

Pi and  ai  denote  respectively i�th  order  autocorrelation  and partial�autocorrelatjon  coefficient  estimates.

## J  oao Victor Issler

The  next step was to model the conditional returns taking into account the fact that they are heteroskedastic.  The latter is done by fitting  the  data  to  a  wide  variety  of  popular models of the  ARCH class.  From the results of this exercise, some stylized facts  will sur­ face,  being an important component of a later modelling effort.  Be­ cause of the evidence of non-Gaussian returns, the covariance-matrix correction proposed by Bollerslev and Wooldridge (1992) is employed when the Normal density is used in estimation. The conditional mean of  all  returns included  only  a constant term,  since  returns  show  no obvious autocorrelation structure. This choice seems  appropriate, since,  when testing the significance of autoregressive and/or moving­ average terms for ARCH-model estimates (not reported here)  the null of a zero coefficient is accepted in all cases. 11

Estimation results for the return on the US$ are presented in ta­ ble 2.  We first ran a G4RCH(l, 1) model assuming Gaussian errors. The unit-root test ( a +,B  = 1 in this case) does not reject the null at usual significance levels (p-value of 0.35).  With the exception of the Gaussian T ARCH model, the same is observed for all other models used.  The EG4RCH(l, 1) model with Gaussian errors shows no sign of asymmetry of shocks, since the coefficient of E't-I ! CTt-l is not sig­ nificant.  When the GED is used instead of the Normal, we find some evidence of asymmetry, but it is against the leverage effect.  Similar but weaker evidence is also found for the Gaussian T ARCH model. Compared to the Gaussian case, there is an improvement in the AIC and BIC criteria when we use the Student-t or the GED distributions for the error in the G4RCH(l, 1) and the EG4RCH(l, 1) model re­ spectively.  The estimated degrees of freedom are relatively low (2.64 and 0.98 respectively), a clear sign of leptokurtosis.'2  Hence, we have

Estimating and Forecasting the Volatility of Brazilian Finance Series evidence of fat tails for the conditional distribution,  possibly a unit

root for the conditional variance, and weak evidence of asymmetry.

| Thble 2  Basic ARCH Estimates for the Return on the US$   | Thble 2  Basic ARCH Estimates for the Return on the US$   | Thble 2  Basic ARCH Estimates for the Return on the US$   | Thble 2  Basic ARCH Estimates for the Return on the US$   | Thble 2  Basic ARCH Estimates for the Return on the US$   | Thble 2  Basic ARCH Estimates for the Return on the US$   | Thble 2  Basic ARCH Estimates for the Return on the US$   |
|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| Mean                                                      | Constant                                                  | 0.028  (13.41)                                            | 0.031  (9.03)                                             | 0.024  (15.73)                                            | 0.019  (18.13)                                            | 0.029  (14.42)                                            |
| Variance                                                  | Constant                                                  | 9.96.E-5  (1.51)                                          | ·0.32  (-3.98)                                            | 0.0002  (2.72)                                            | 166.91  (0.02)                                            | 8.3BE-5  (1.40)                                           |
|                                                           | eLL                                                       | 0.220  (3.37)                                             |                                                           | 0.280  (3.37)                                             |                                                           | 0.300  (3.89)                                             |
|                                                           | dt-l,eLl                                                  |                                                           |                                                           |                                                           |                                                           | -0.18  (-1.76)                                            |
|                                                           | a1-1                                                      | 0.800  (16.22)                                            |                                                           | 0.820  (33.26)                                            |                                                           | 0.810  (19.35)                                            |
|                                                           | [£t\_11/O"t\_1                                              |                                                           | 0.390  (4.13)                                             |                                                           | 0.150  (7.81)                                             |                                                           |
|                                                           | et-t/at-t                                                 |                                                           | 0.090  (1.37)                                             |                                                           | 0.430  (2.69)                                             |                                                           |
|                                                           | In(.L)                                                    |                                                           | 0.990  (126.41)                                           |                                                           | 0.999  (443.99)                                           |                                                           |
| Estimation  Method                                        |                                                           | ML                                                        | ML                                                        | ML                                                        | ML                                                        | ML                                                        |
| Model                                                     |                                                           | GARCH I,I ( )                                             | EGARCH I,I ( )                                            | GARCH I,I ( )                                             | EGARCH I,I ( )                                            | TARCH I,l ( )                                             |
| Distribution                                              |                                                           | N(.)                                                      | N(·)                                                      | t · ( )                                                   | GED                                                       | N(.)                                                      |
| Log L                                                     |                                                           | 872.31                                                    | 876.79                                                    | 945.66                                                    | 931.  75                                                  | 882.56                                                    |
| AIC                                                       |                                                           | -1.6714                                                   | -1.6781                                                   | -1.8107                                                   | -1.7820                                                   | -1.6890                                                   |
| BIC                                                       |                                                           | -1.6524                                                   | -1.6543                                                   | -1.7869                                                   | -1.7530                                                   | -1.6650                                                   |
| Sample                                                    |                                                           | 8/7/94  1/7/98                                            | 8/7/94  1/7/9B                                            | 8/7/94  1/7/98                                            | 8/7/94  1/7/94                                            | 8/7/94  1/7/98                                            |
| Unit-root test  (P-value)                                 |                                                           | 0.350                                                     | 0.450                                                     | 0.170  2.640                                              | 0.980  0.820                                              | 0.047                                                     |
| Degrees of  of freedom                                    |                                                           |                                                           |                                                           | (10.82)                                                   | (22.25)                                                   |                                                           |

Notes:

Because of the suspicion of a change in target-zone regimes noted earlier, we should be cautious about the evidence of asymmetry and of  a  unit  root  for  the  conditional  variance. Indeed,  Hamilton and

## J  oao Victor Issler

Susmel (1994) point out that a structural break in the variance series may induce a unit root for it. Ignoring changes in regimes may also induce  the  spurious impression that volatility is related to returns. This may happen because returns may differ for the two target-zone regimes.'3

Estimation  results  for  the  return  of  the  Cbond  are  presented in  table 3. We find  evidence  of asymmetry in the  variance  for  the Gaussian EGARCH(l, 1),  the GED EGARCH(l, 1),  and the Gaus­ sian T ARCH(l, 1). All  indicate  the  presence  of  the  leverage  ef­ fect. As suspected from earlier tests, the distribution of the returns has  fat  tails: the  estimated  degrees  of  freedom  for  the  Student-t GARCH(l, l)  and  the  GED  EGARCH(l, l)  are  3.71  and 1.01 re­ spectively.  The latter is statistically different from two in hypothesis testing,  corroborating our previous  finding of  leptokurtosis. If  the asymmetric  effect  is  not  taken  into  account  the  unit-root  test  re­ jects  the null,  but  the  opposite  happens  when it is  considered.  We conel  ude  that there is evidence of asymmetry, favoring the leverage effect,  heavy tails for the conditional distribution, and no clear sign of a unit root for the conditional variance.

For the  return on COCOA  we find no asymmetry at  all,  some evidence of a unit root for the conditional variance, and fat tails; see results in table 4. The estimated degrees of freedom for the Student-t and GED distributions are respectively  3.32 and 0.977.  The latter rejects  Normality  with high confidence  in  hypothesis  testing. It  is also interesting to note that, regardless of the distribution used, unit­ root evidence is not present when we use the EGARCH(l, 1) model.

Estimating and Forecasting the Volatility of Brazilian Finance Series

| Table 3  Basic ARCH Estimates for the Return on the CBOND   | Table 3  Basic ARCH Estimates for the Return on the CBOND   | Table 3  Basic ARCH Estimates for the Return on the CBOND   | Table 3  Basic ARCH Estimates for the Return on the CBOND   | Table 3  Basic ARCH Estimates for the Return on the CBOND   | Table 3  Basic ARCH Estimates for the Return on the CBOND   | Table 3  Basic ARCH Estimates for the Return on the CBOND   |
|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| Mean                                                        | Constant                                                    | 0.134  (3.72)                                               | 0.008  (2.09)                                               | 0.150  (4.51)                                               | 0.098  (3.31)                                               | 0.080  (2.05)                                               |
| Variance                                                    | Constant                                                    | 0.092  (2.15)                                               | -0.15  (-3.08)                                              | 0.062  (2.94)                                               | 1.20  (5.12)                                                | 0.139  (3.05)                                               |
|                                                             | d\_l                                                         | 0.180  (1.66)                                               |                                                             | 0.110  (4.70)                                               |                                                             | 0.030  (1.42)                                               |
|                                                             | dt\_l  .  ef-l  aLL                                          |                                                             |                                                             |                                                             |                                                             | 0.23  (2.02)                                                |
|                                                             |                                                             | 0.810  (10.08)                                              |                                                             | 0.880  (41.92)                                              |                                                             | 0.800  (14.32)                                              |
|                                                             | !et\_l!/Ut\_l                                                 |                                                             | 0.270  (3.01)                                               |                                                             | 0.170  (4.98)                                               |                                                             |
|                                                             | C.t\_l/rYt\_l  I n { cr L l )                                 |                                                             | -0.15  (-2.55)  0.930                                       |                                                             | -0.47  (-2.82)  0.960                                       |                                                             |
| Estimation  Method                                          |                                                             | ML                                                          | ML                                                          | ML                                                          | ML                                                          | ML                                                          |
| Model                                                       |                                                             | GARCH(l,l)                                                  | EGARCH(l,l)                                                 | GARCH(l,l)                                                  | EGARCH(l,l)                                                 | TARCH(l,l)                                                  |
| Distribution                                                |                                                             | NO                                                          | NO                                                          | t o                                                         | GED                                                         | N(.)                                                        |
| AlC                                                         |                                                             | 3.6661                                                      | 3.6323                                                      | 3.5352                                                      | 3.553                                                       | 3.630                                                       |
| BIC                                                         |                                                             | 3.6844                                                      | 3.6551                                                      | 3.5439                                                      | 3.580                                                       | 3.653                                                       |
| Sample                                                      |                                                             | 22/4/94  1/7/98                                             | 22/4/94  1/7/98                                             | 22/4/94  1/7/98                                             | 22/4/94  1/7/94                                             | 22/4/94  1/7/98                                             |
| Unit-root test                                              |                                                             | 0.680                                                       | 0.005                                                       | 0.630                                                       | 0.0008                                                      | 0.0006                                                      |
| (P-value)                                                   |                                                             |                                                             |                                                             | 3.710                                                       | 1.010                                                       |                                                             |
| Degrees of  of freedom                                      |                                                             |                                                             |                                                             | (8.47)                                                      | (24.06)                                                     |                                                             |

Note":

- (2)  Gflu:J3inn  EGARCH(l,l) estimlltc::&lt; cqu"tion (15),  while  EGARCH{l,l) with  the GED  specificati o n estim"l.&lt;m  equntion  (16);

For the return on Telebras we definitely find asymmetry, favoring the leverage effect; see the results in table 5.  This happens regardless of the model or distribution used.  There is also a weak sign of a unit root,  again  rejected  whenever  asymmetry  is  considered. Evidence of  fat  tails is weaker than that for other series,  since the estimated degrees  of  freedom  for the  Student-t and GED  distribution are re-

## J  oao Victor Issler

spectively 6.81 and 1.41. However, formal statistical testing rejected the Normal distribution again when the GED specification is used.

| Table  4  Basic ARCH Estimates for the Return on COCOA   | Table  4  Basic ARCH Estimates for the Return on COCOA   | Table  4  Basic ARCH Estimates for the Return on COCOA   | Table  4  Basic ARCH Estimates for the Return on COCOA   | Table  4  Basic ARCH Estimates for the Return on COCOA   | Table  4  Basic ARCH Estimates for the Return on COCOA   | Table  4  Basic ARCH Estimates for the Return on COCOA   |
|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| Mean                                                     | Constant                                                 | 0.029  (0.94)                                            | 0.065  (1.94)                                            | ·0.140  (·0.57)                                          | 0.000  (0.00)                                            | 0.037  (1.19)                                            |
| Variance                                                 | Constant                                                 | 0.017  (2.03)                                            | ·0.050  (-3.11)                                          | 0.036  (3.35)                                            | ·5.68  (-1.70)                                           | 0.016  (2.03)                                            |
|                                                          | e L l                                                    | 0.030  (3.99)                                            |                                                          | 0.040  (4.55)                                            |                                                          | 0.040  (2.03)                                            |
|                                                          | 0-[\_1                                                    | 0.960  (119.42)                                          |                                                          | 0.950  (115.10)                                          |                                                          | 0.960  (128.05)                                          |
|                                                          | let\_ll/Ut\_l                                              |                                                          | 0.081  (3.54)  0.010                                     |                                                          | 0.044  (4.64)  0.21                                      |                                                          |
|                                                          | e t\_t/Ot\_ l  In(o"Ld                                     |                                                          | (0.54)  0.993  (247.04)                                  |                                                          | (0.96)  0.995  (364.97)                                  |                                                          |
| Estimation  Method                                       |                                                          | ML                                                       | ML                                                       | ML                                                       | ML                                                       | ML                                                       |
| Model  Distribution                                      |                                                          | NO                                                       | GARCH(l,l)  EGARCH(l,l)  N(·)                            | t(.)                                                     | GARCH(l,l)  EGARCH(l,l)  TARCH(l,l)  GED                 | N(·)                                                     |
| Log L                                                    |                                                          | -4078.65                                                 | ·4090.70                                                 | -3910.23                                                 | -3889.42                                                 | 4077.27                                                  |
| AlC                                                      |                                                          | 3.6947                                                   | 3.7065                                                   | 3.5432                                                   | 3.519                                                    | 3.694                                                    |
| BIC                                                      |                                                          | 3.7050                                                   | 3.7194                                                   | 3.5561                                                   | 3.534                                                    | 3.707                                                    |
| Sample                                                   |                                                          | 11/10/90  1/7/98                                         | 11/10/90  1/7/98                                         | 11/10/90  1/7/98                                         | 5/1/90  1/7/94                                           | 8/7/94  1/7/98                                           |
| Unit-root test  (P.value)                                |                                                          | 0.20                                                     | 0.07                                                     | 0.30                                                     | 0.08                                                     | 0.9119                                                   |
| Degrees of  of  freedom                                  |                                                          |                                                          |                                                          | 3.320  (11.61)                                           | 0.977  (30.13)                                           |                                                          |

Ncte�:

We now turn to SW ARCH-model estimation.  First,  we  enter­ tained the two-regime model, with St = 1 for the low-variance regime,

with gl normalized to unity,  and  with St = 2 when the variance is g2 greater than that in regime one. Tables 6 through 9 present estimates using  the SW ARCH  model for  all four series.  Following Hamilton and  Susmel  (1994),  we  considered  only  the  case  of  Student-t  and Normal densities.

5

Nows:

| Table  Basic  ARCH Estimates for the Return on TELEBRAS   | Table  Basic  ARCH Estimates for the Return on TELEBRAS   | Table  Basic  ARCH Estimates for the Return on TELEBRAS   | Table  Basic  ARCH Estimates for the Return on TELEBRAS   | Table  Basic  ARCH Estimates for the Return on TELEBRAS   | Table  Basic  ARCH Estimates for the Return on TELEBRAS   | Table  Basic  ARCH Estimates for the Return on TELEBRAS   |
|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| Mean                                                      | Constant                                                  | 0.280  (4.28)                                             | 0.180  (2.55)                                             | 0.280  (4.02)                                             | 0.156  (2.22)                                             | 0.177  (2.53)                                             |
| Variance                                                  | Constant                                                  | 0.35  (3.23)                                              | -0.07  (-1.87)                                            | 0.33  (3.24)                                              | 2.10  (14.19)                                             | 0.52  (3.99)                                              |
|                                                           | eLL                                                       | 0.180  (3.97)                                             |                                                           | 0.190  (5.64)                                             |                                                           | 0.040  (1.45)                                             |
|                                                           | dt\_l  .  e:;-1                                            |                                                           |                                                           |                                                           |                                                           | 0.22  (3.40)                                              |
|                                                           | 0"; \_1                                                    | 0.790  (19.30)                                            |                                                           | 0.790  (24.15)                                            |                                                           | 0.790  (19.85)                                            |
|                                                           | let\_ll/O"t\_1                                              |                                                           | 0.260  (4.55)                                             |                                                           | 0.240  (6.07)                                             |                                                           |
|                                                           | et\_l/O"t\_l                                                |                                                           | -0.15  (-3.69)                                            |                                                           | -0.50  (-2.98)                                            |                                                           |
| Estimation  Method                                        |                                                           | ML                                                        | ML                                                        | ML                                                        | ML                                                        | ML                                                        |
| Model                                                     |                                                           | GARCH(I,I)                                                | EGARCH(I,I)                                               | GARCH(I,I)                                                | EGARCH(I,I)                                               | TARCH(I,I)                                                |
| Distribution                                              |                                                           | NO                                                        | N(·)                                                      | t(.)                                                      | GED                                                       | N(·)                                                      |
| Log L                                                     |                                                           | -2498.84                                                  | -2483.38                                                  | -2485.67                                                  | -2488.63                                                  | -2483.45                                                  |
| A1C                                                       |                                                           | 4.8178                                                    | 4.7899                                                    | 4.7944                                                    | 4.8020                                                    | 4.7900                                                    |
| BIC                                                       |                                                           | 4.8368                                                    | 4.8137                                                    | 4.8034                                                    | 4.8310                                                    | 4.8100                                                    |
| Sample                                                    |                                                           | 8/7/94  1/7/98                                            | 8/7/94  1/7/98                                            | 8/7/94  1/7/98                                            | 8/7/94  1/7/94                                            | 8/7/94  1/7/98                                            |
| Unit-root test  (P-value)                                 |                                                           | 0.120                                                     | 0.000                                                     | 0.360                                                     | 0.00003                                                   | 0.0000                                                    |
| Degrees of  of freedom                                    |                                                           |                                                           |                                                           | 6.810  (4.96)                                             | 1.410  (17.52)                                            |                                                           |

- (1) t-lIW.t!�tiCll in parentheseu,
- (3) Cllull3iAn GARCH{l,l), TARCH(l,l)  and EGARCH(l,l) ClIUm"'WlI U!I&lt;! the Bol!er!lev ",nd Wooldddge (1992) que.sl-ml&gt;Ximum  likelihood Mymptotie variance-&lt;:oY'lld",nee  mAtrix.
- (2) Gaussian  EGARCH(l,l) e!tlmAwll &lt;lqulltlon (15), while EGARCH(l,l) with the CED opeclfieation estimew! equation (16);

## J  oao Victor IssIer

## Two-regime SWARCH and SWARCHL Estimates for the Return of the US$

| Constant  (mean)                         | 0.026  (0.002)           | 0.026  (0.002)  0.02     | 0.026  (0.002)           | 0.022  (0.002)           | 0.022  (0.002)             | 0.022  (0.002)           |
|------------------------------------------|--------------------------|--------------------------|--------------------------|--------------------------|----------------------------|--------------------------|
| AR(l)                                    |                          | (0.03)                   |                          |                          |                            |                          |
| Constant  (variance)                     | 0.001  (0.0002)          | 0.001  (0.0001)          | 0.002  (0.0002)          | 0.003  (0.0007)          | 0.003  (0.0007)            | 0.002  (0.0005)          |
| �  -1  ut                                | 0.27  (0.06)             | 0.27  (0.06)             | 0.30  (0.08)             | 0.39  (0.14)             | 0.39  (0.14)               | 0.35  (0.11  )           |
| UF-2                                     | 0.19  (0.05)             | 0.20  (0.05)             | 0.21  (0.06)             | 0.26  (0.11)             | 0.26  (0.11)               | 0.17  (0.08)             |
| Uf-3                                     | 0.08  (0.04)             | 0.08  (0.04)             |                          |                          | 0.01  (0.03)               | 0.000  (0.05)            |
| �  u t \_ 4                               | 0.18  (0.05)             | 0.17  (0.05)             |                          |                          |                            | 0.15  (0.07)             |
| Degrees  of freedom                      |                          |                          |                          | 2.77  (0.30)             | 2.78  (0.30)               | 3.02  (0.35)             |
| g 2                                      | 98.23  (18.12)           | 98.84  (18.04)           | 106.77  (15.60)          | 130.75  (24.91)          | 130.36  (25.02)            | 132.01  (26.80)          |
| Pll                                      | 0.99  (0.005)            | 0.989  ( * )             | 0.983  ( * )             | 0.999  ( * )             | 0.999  ( * )               | 0.999  ( * )             |
| P22                                      | 0.97  (0.011)            | 0.973  ( * )             | 0.959  ( * )             | 0.998  ( * )             | 0.999  ( * )               | 0.999  ( * )             |
| Erg. PI   Erg' P 2  Log  L  Distribution | 0.71  0.29  904.39  N(-) | 0.71  0.29  897.32  N(·) | 0.71  0.29  883.07  N(·) | 0.64  0.36  961.62  t(·) | 0.64  0.36  961.64  t( . ) | 0.63  0.37  968.72  t(-) |

Notes:

## Estimating and Forecasting the Volatility of Brazilian Finance Series

## Two-regime SWARCH and SWARCHL Estimates for the Return of the CBOND

| Constant  ( mean )  AR l ( )           | 0.15  (0.04)                  | 0.14  (0.04)               | 0.13  (0.04)  0.01  (0.03)   | 0.14  (0.04)  0.03  (0.03)     | 0.14  (0.04)                   |
|----------------------------------------|-------------------------------|----------------------------|------------------------------|--------------------------------|--------------------------------|
| Constant  ( variance )  ut-l           | 0.43  (0.08)  0.03  (0.06)    | 0.44  (0.08)  0.05  (0.06) | 0.44  (0.07)  0.13  (0.07)   | 0.43  (0.11)  0.06  (0.08)     | 0.45  (0.11)  0.07  (0.08)     |
| ut-2                                   | 0.17  (0.06)                  | 0.16  (0.06)               | 0.28  (0.06)                 | 0.15  (0.06)                   | 0.15  (0.06)                   |
| ut-3                                   | 0.19  (0.07)                  | 0.22  (0.06)               |                              | 0.22  (0.07)                   | 0.21  (0.06)                   |
| Uf-4                                   | 0.06  (0.04)                  |                            |                              |                                |                                |
| Degrees  of freedom                    |                               |                            |                              | 16.22  (26.27)                 | 13.92  (18.01)                 |
| g2                                     | 5.64  (0.80)                  | 5.56  (0.77)               | 6.08  (0.75)                 | 4.97  (1.27)                   | 4.80  ( 1.26)                  |
| dt-1  .  ur-l                          | 0.37  (0.11)                  | 0.38  (0.11)               | 0.33  (0.12)                 | 0.41  (0.12)                   | 0.40  (0.12)                   |
| Pll                                    | 0.78  (0.08)                  | 0.75  (0.10)               | 0.69  (* )                   | 0.77  (0.24)                   | 0.66  (0.23)                   |
| P22                                    | 0.37  (0.13)                  | 0.35  (0.12)               | 0.37  (* )                   | 0.38  (0.15)                   | 0.35  (0.16)                   |
| Erg. P!  Erg' P 2  Log L  Distribution | 0.74  0.26  -1942.91  N . ( ) | 0.72  0.28  -1944.22  NO   | 0.67  0.33  -1953.43  NO     | 0.65  0.35  -1943.26  t ( .  ) | 0.66  0.34  -1943.74  t ( )  · |

Notes:

## Jo;;o Victor Issier

## Two-regime SWARCH and SWARCHL Estimates for the Return of COCOA

|                      |                |               | -0.01        | -0.01        | -0.01  (0.03)   | -0.001        | -0.007        | -0.006       |
|----------------------|----------------|---------------|--------------|--------------|-----------------|---------------|---------------|--------------|
| Constant  (mean)     | -0.001  (0.01) | -0.01  (0.03) | (0.03)       | (0.03)       | -0.02           | (0.02)        | (0.02)        | (0.02)       |
| AR(l)                |                |               |              |              | (0.02)          |               |               |              |
| Constant  (variance) | 0.76  (0.11)   | 0.76  (0.11)  | 0.72  (0.09) | 0.72  (0.08) | 0.73  (0.08)    | 1.43  (0.18)  | 1.44  (0.17)  | 1.49  (0.17) |
| UZ-l                 | 0.17  (0.05)   | 0.14  (0.06)  | 0.14  (0.06) | 0.11  (0.05) | 0.13  (0.05)    | 0.08  (0.03)  | 0.08  (0.03)  | 0.08  (0.03) |
| ur-2                 | 0.05  (0.05)   | 0.04  (0.04)  | 0.01  (0.02) | 0.02  (0.03) | 0.02  (0.04)    | 0.000  (0.03) | 0.000  (0.02) |              |
| ur-3                 |                |               | 0.15  (0.04) | 0.12  (0.04) | 0.12  (0.04)    | 0.03  (0.03)  | 0.03  (0.03)  |              |
| UZ-4                 |                |               |              | 0.13  (0.04) | 0.12  (0.04)    | 0.03  (0.04)  |               |              |
| Degrees  of freedom  |                |               |              |              |                 | 3.55  (0.33)  | 3.58  (0.33)  | 3.58  (0.33) |
| g,  .                | 7.91  (0.69)   | 7.89  (0.68)  | 8.04  (0.76) | 8.16  (0.87) | 8.27  (0.90)    | 2.86  (0.40)  | 2.85  (0.32)  | 2.88  (0.32) |
| dt\_l  .  Ut\_ !  -2   |                | 0.05  (0.09)  | 0.05  (0.07) | 0.04  (0.07) |                 |               |               |              |
| Pll                  | 0.76  ( *)     | 0.76  (*)     | 0.79  (*)    | 0.84  ( *)   | 0.84  (*)       | 0.996  (*)    | 0.996  (*)    | 0.996  (*)   |
| P22                  | 0.30  ( *)     | 0.31  (*)     | 0.26  (*)    | 0.24  (*)    | 0.24  (*)       | 0.994  (*)    | 0.995  (*)    | 0.994  (*)   |
| Erg. PI              | 0.75           | 0.74          | 0.78         | 0.83         | 0.83            | 0.62          | 0.61          | 0.61         |
| Erg' P 2             | 0.25           | 0.26          | 0.22         | 0.17         | 0.17            | 0.38          | 0.39          | 0.39         |
| Log L                | -3981.12       | -3980.91      | -3974.06     | -3968.02     | -3974.15        | -3912.25      | -3912.90      | -3913.44     |
| Distribution         | N O            | NO            | N(·)         | N O          | N(·)            | t o           | t o           | t o          |

## Estimating and Forecasting the Volatility of Brazilian Finance Series

Table 9 Two-regime SWARCH and SWARCHL Estimates for  the Return of TELEBRAS

| Constant  (mean)  AR(I)               | 0.2S  (0.07)             | 0.17  (0.06)  0.01  (0.03)   | O.IS  (0.06)                 | 0.25  (0.  OS)             | 0.27  (0.07)             | 0.27  (0.07)                 | 0.27  (0.07)                 |
|---------------------------------------|--------------------------|------------------------------|------------------------------|----------------------------|--------------------------|------------------------------|------------------------------|
| Constant  (variance)                  | 2.25  (0.27)             | 0.10  (0.03)                 | 0.10  (0.03)                 | 0.30  (0.19)               | 1.97  (0.31)             | 2.17  (0.31)                 | 2.41  (0.31)                 |
| Ui-l                                  | 0.000  (0.03)            | 0.03  (0.1)                  | 0.03  (0.04)                 | 0.02  (0.04)               | 0.000  (0.02)            | 0.000  (0.02)                | 0.001  (0.03)                |
| ur-2                                  | 0.17  (0.04)             | 0.20  (0.06)                 | 0.20  (0.05)                 | 0.22  (0.06)               | 0.17  (0.05)             | 0.16  (0.05)                 | (0.17)  (0.05)               |
| ur-3                                  |                          | O.lS  (0.06)                 | O.IS  (0.05)                 | 0.16  (0.05)               | 0.07  (0.04)             | 0.07  (0.04)                 |                              |
| Uf-4                                  |                          | 0.22  (0.06)                 | 0.22  (0.06)                 |                            | 0.09  (0.05)             |                              |                              |
| Degrees  of freedom                   |                          |                              |                              |                            | 10.01  (3.11)            | 10.93  (3.81)                | 11.33  (4.06)                |
| g2                                    | 4.25  (0.57)             | 23.41  (7.64)                | 22.75  (7.25)                | 13.16  (7.15)              | 3.50  (0.61)             | 3.54  (0.58)                 | 3.S7  (0.59)                 |
| dt-1  .  ur-l                         | 0.33  (O.OS)             | 0.37  (0.11)                 | 0.37  (0.10)                 | 0.44  (0.11)               | 0.30  (0.09)             | 0.31  (0.09)                 | 0.31  (0.09)                 |
| PH                                    | 0.98  (0.009)            | 0.43  (0.10)                 | 0.44  (0.10)                 | 0.40  (0.13)               | 0.99  (0.01)             | 0.99  ( * )                  | 0.99  (0.007)                |
| P22                                   | 0.98  (0.01)             | 0.93  (0.02)                 | 0.93  (0.02)                 | 0.90  (0.04)               | 0.99  (0.01)             | 0.99  ( * )                  | 0.99  (0.008)                |
| Erg. P,  Erg' P2  Log L  Distribution | 0.48  0.52  -2485.63  NO | 0.11  0.89  -2490.41  N(·)   | 0.11  0.89  -2484.14  N( . ) | 0.15  0.85  -2500.07  N(·) | 0.41  0.58  -2475.90  to | 0.42  0.58  -2478.36  t(·  ) | 0.47  0.53  -2481.17  t(·  ) |

Notes:

## Jollo Victor IssIer

For the return of the US$, including a first-order autoregressive term  for  the  return  did  not  improve estimation results  at  all. For the  Gaussian  SW ARCH(2, 2)  model,  the  t-test  for the  significance of the AR(l) coefficient yields a statistic of 0.67,14  not significant at usual  levels. 15 There  is  no  evidence  of  asymmetry  in  the  variance either  the  t-statistic  for  the  leverage  coefficient  is  virtually  zero. Overall,  our preferred  model is the  SW ARCH(2, 4),  whereas  using a Student-t density yields a much higher maximized likelihood value than using the Normal, at the cost of just one more degree of free­ dom. Indeed,  the  likelihood-ratio  test  statistic  for  comparing  the Student-t density with the Normal for the SW ARCH(2, 4) model is -2 x (904.39 - 968.72) = 128.66, overwhelmingly significant at any reasonable level.  Finally, the preferred model for the return on the US$ has a variance in regime two 132.01 times higher than that in the low-variance regime (regime 1).

When the Student-t density was used, the estimated transition probability matrix was most of the time in the boundary of its con­ straint.  The  same is reported for  some estimates in Hamilton and Susmel  (1994,  footnote  5). To avoid  meaningless  probability  esti­ mates,  the  model  was reparameterized to ensure that  0 � Pij � 1, and 2::; =1 Pij = 1.  Since calculating the respective pwestimate stan­ dard errors is time consuming, we refrain from doing it here.

For  the return  on  the Cbond  our  preferred  models  is  the SW ARCH - L(2, 3); notice that the coefficient of the fourth lagged

squared error is not significant.  Conforming to our previous evidence, the leverage effect for the Cbond is  confirmed using  a t-ratio  test: 3.45 and 3.33 when using the Student-t and Normal densities respec­ tively.  Also based on a t-test,  including a first-order  autoregressive term for the return is insignificant, with a t-ratio of 1.  When testing which density to use, the likelihood-ratio test statistic for comparing the Student-t density  with the Normal for the SW ARCH - L(2, 3) model is  -2 x [-1944.22 - (-1943.74)] = 0.96,  which is not signif­ icant  at  usual  levels. Thus,  it makes little difference  which one  is chosen here. Given our  estimate of g2, Cbond volatility in regime 2 is  about  2.2 times higher than that of regime 1; notice that g2 is statistically different than one at usual levels.

For the return on COCOA our preferred models were the Gaus­ sian SW ARCH(2, 4) and the Student-t SW ARCH(2, 1). ' 6 Confirm­ ing  our  previous results,  there is no  asymmetry  in the variance;  a t-ratio smaller than 1 for the leverage coefficient.  As it happened for the  return  of  the  US$,  the  estimated  transition  probability matrix was  most of  the time in the boundary of  its  constraints  when the Student-t density was used, which lead to the estimation of a repa­ rameterized model for which  we do not report standard errors for probability estimates.  Last,  when we compared the Student-t with the Normal for the SW ARCH(2, 4), the likelihood-ratio test statistic was -2 x [-3968.02 "'; (-3912.25)] = 111.54, which overwhelmingly significant  at  usual  levels. Therefore  it seems  more appropriate  to use  the  Student-t  distribution.!7 Given  our  estimate  of g2 for  the

Student-t SW ARCH(2, 1),  COCOA  volatility  in  regime  2  is  about 1.  7 times higher than that of regime 1; notice that 92 is statistically different than one at usual levels.

For the return on Telebras our preferred models is the SW ARCH - L(2, 4).  Comparing the Student-t to the Normal yields a  likelihood-ratio test statistic  of  -2 x [-2484.14 - (-2475.90)] = 16.48,  which  is  significant  at  usual  levels. The  key  difference  be­ tween Student-t- and Gaussian-density estimates is in the transition probability-matrix parameters. For the Gaussian case, PH = 0.44 and ih2 = 0.93, whereas for the Student-t PH = 0.99 and P22 = 0.99. The scale parameter and the volatility constant are also different for the two specifications.  For the  Student-t 112 = 3.50  and aD = 1.97, while for the Gaussian case 712 = 22.75 and aD = 0.10.  Given our es­ timate of 92 for the Student-t SW ARCH  -L(2, 4), Telebras volatility in regime 2 is about  1.9 times higher than that of regime 1;  notice that 92 is statistically different than one at usual levels.  Conforming to  our  previous  evidence,  the  leverage  effect  is present  and signifi­ cant for all estimated models.  For our preferred model, the leverage coefficient is 0.30, with a t-ratio of 3.33.

A last modelling effort is made using SW ARCH models, in which a three-regime model is entertained.  Following Hamilton and Susmel the goal is to allow for an extra regime to capture extreme outliers in the data set; see their discussion in pp. 327-330.  This may be use­ ful for Brazilian data since the chances of observing outliers here are much higher than those in developed economies.  Estimates using the Gaussian density are reported in table 10 for the returns of the US$, the Cbond, and Telebras.  Due to convergence problems, neither re­ turns on COCOA could be estimated using a Gaussian specification, nor could be returns on any of the assets using the Student-t density.

## Estimating and Forecasting the Volatility of Brazilian Finance Series

Table 10 Two-regime SWARCH and SWARCHL Estimates with Gaussian Errors

|                         | R$              | CBOND              | TELEBRAS     |
|-------------------------|-----------------|--------------------|--------------|
| Constant  (mean)  AR(I) | 0.026  (0.002)  | 0.13  (0.04)  0.01 | 0.27  (0.07) |
| Constant  (variance)    | 0.001  (0.0001) | 0.56  (0.07)       | 2.22  (0.28) |
| UZ-l                    | 0.26  (0.06)    | 0.14  (0.07)       | 0.02  (0.04) |
| ur-2                    | 0.12  (0.06)    | 0.11  (0.04)       | 0.15  (0.05) |
| g2                      | 5.54  (1.26)    | 2.05  (0.33)       | 2.92  (0.61) |
| g3                      | 153.25  (23.06) | 8.63  (1.57)       | 6.45  (1.50) |
| dt-1  . ur-l            |                 | 0.38  (0.11)       | 0.32  (0.09) |
| P11                     | 0.99  ( * )     | 0.98  ( * )        | 0.98  ( * )  |
| Pz2                     | 0.94  ( * )     | 0.60  ( * )        | 0.61  ( * )  |
| Erg.P!                  | 0.60            | 0.37               | 0.44         |
| Erg.P2                  | 0.15            | 0.45               | 0.40         |
| Log L                   | 909.67          | -1946.38           | -2482.63     |
| Distribution            | NO              | N(·)               | N( )         |

Notes:

Following our  previous  results, the returns on the Cbond and  Telebras  allow  for  the  leverage  effect. To  make  numeri­ cal  estimation  feasible, The  order  of  the  ARCH  models  had  to

be limited  to  two,'· which  resulted in a SW ARCH  - L{3, 2) model for the returns on the Cbond  and  Telebras, and a SW ARCH{3, 2)  model  for  the  return  on  COCOA.  The three­ regime  models  were  tested  against  their  two-regime  counterparts using the likelihood-ratio test statistic'9 The latter is -2 x [883.07 - (909.67)] = 53.20,  -2 x [-1953.42 - (-1946.38)] = 14.08, and  -2 x [-2485.63 - (-2482.63)] = 6.00,  for  their  return on  the US$,  on  the  Cbond  and  on  Telebras  respectively. Under  correct specification, these test statistics are asymptotically distributed chi­ squared with 3,  2,  and 1  degrees of freedom respectively,  rejecting the two-regime models at 5% significance.

## 4.3.  Comparing  different  ARCH-model  estimates

This Section focus on comparing goodness-of-fit and forecasting accuracy for ARCH-models. The goodness-of-fit statistics used here are  all  likelihood  based. In  particular,  we  consider  the  maximum of  the  log-likelihood function,  and the Akaike  (1973)  and  Schwarz (1978)  information criteria, which are a function of the former.

Comparing forecasting accuracy of different models that predict the  conditional mean of a  given  variable is  a simple task.  Suppose that we have the sequence {Yt&gt;  Xt } r � N of realizations of random vari­ ables,  where Yt is the realization of the explained variable in a regres­ sion, and Xt is a vector containing realizations of possible explanatory variables for Yt. In principle,  we could consider M different models, indexed by i = 1, · · · M, that hold for the population counterparts of Yt, Xt with error Ei:

<!-- formula-not-decoded -->

where t  = 1, · ·  T. · Based  on  some  optimality  criteria,  these  M models  could  be  estimated,  resulting  in 13 i -model  i's  estimate for the  conditional-mean  parameter  {3;. Conditional  on Xt, for t  = T + 1, . . . N, the  out-of -sample  f orecasting  accuracy  of  these M models  could  be  compared  using some loss-function.  In partic­ ular, if the  mean-squared-error function is considered, the following statistic for all M models could be calculated:

<!-- formula-not-decoded -->

Under the  usual caveats,  the  "best"  model would  be the one with the smallest value for (31).

Unfortunately,  this same procedure cannot be replicated if the goal is to measure forecasting accuracy for the conditional variance (the  same  applies  to volatility). This  happens  because  the  condi­ tional variance  is  not  a  random variable  for  which  we  can  collect realizations to  form statistics such as  (31).  On the contrary, a t is an  unknown  time-varying parameter  that  could,  at  best,  be  esti­ mated consistently when the true Data Generating Process  (DGP) is known.  In general, since the DGP is unknown, there is no hope of even getting a consistent estimate.

Recognizing this problem, different authors have proposed track­ ing down not the conditional variance but some other variable, which may be the  same  for  all  volatility  forecasts. For  example,  Heynen and Kat (1994)  use what they label  "realized volatility" , a degrees­ of-freedom  corrected  version  of  (27). Others  have proposed  using implicit volatility; see Engle and Mustafa(1992).  On the other hand, using the definition of conditional variance,  i.e., a t = E[c�  l Ot-I], Hamilton and Susmel propose comparing each model's variance fore­ cast  with what it is supposed to track down.

## J  oao Victor Issler

Thinking in terms of one-step-ahead forecast errors, they propose comparing 0-; with €�, using their respective  estimates. We  follow Hamil  ton and Susmel in assessing the forecast accuracy of our volatil­ ity  estimates  by  using  four different  loss  functions: mean-squared­ error (MSE), mean-absolute-error (MAE), mean-squared-Iog-error [LEj2, and  mean-absolute-Iog-error I LEI. Results  are presented  in tables 11 through 14.

Table  11 Forecast Accuracy of ARCH Models for the Return on the US$

|                  | Loss Function   | Loss Function   | Loss Function   | Loss Function   |
|------------------|-----------------|-----------------|-----------------|-----------------|
| Model            | MSE             | MAE             | [LEJ 2          | I LEI           |
| OL8 Homocedastic | 0.110979        | 0.127350        | 22.13701        | 4.102885        |
| EGARCH(I,I)GED   | 0.099713        | 0.094078*       | 11.72607        | 2.500886        |
| EGARCH(I,I)N(. ) | 0.106856        | 0.100949        | 7.898725*       | 2.088073*       |
| GARCH(I,I)N(·)   | 0.104442        | 0.101210        | 9.653705        | 2.257588        |
| TARCH(I,I)NC)    | 0.108278        | 0.101349        | 8.215606        | 2.124275        |
| GARCH(I,I)t(. )  | 0.123511        | 0.123607        | 9.613312        | 2.467701        |
| SWARCH(2,4)N(·)  | 0.845339        | 0.129706        | 18.81351        | 2.636824        |
| SWARCH(2,4)tO    | 0.162752        | 0.128938        | 9.453510        | 2.391157        |
| SWARCH(3,2)N(·)  | 0.097276*       | 0.096689        | 10.38927        | 2.432782        |

Notes:

<!-- image -->

## Estimating and Forecasting the Volatility of Brazilian Finance Series

Table 12 Forecast Accuracy of ARCH Models for the Return on the CBOND

|                    | Loss Function   | Loss Function   | Loss Function   | Loss Function   |
|--------------------|-----------------|-----------------|-----------------|-----------------|
| Model              | MSE             | MAE             | [LEJ 2          | ILEI            |
| OLS Homocedastic   | 206.2718        | 4.581094        | 12.04767        | 2.608068        |
| EGARCH(I,I)GED     | 192.1416        | 4.077298        | 11.09051        | 2.264638        |
| EGARCH(I,I)N(. )   | 173.8946'       | 3.768738'       | 9.832155        | 2.211236        |
| GARCH(I,I)N(·)     | 191.2182        | 4.191442        | 8.498950        | 2.138627*       |
| TARCH(I,I)N(·)     | 179.9914        | 3.952777        | 9.692357        | 2.209044        |
| GARCH(I,I)t(·)     | 192.8944        | 4.258412        | 8.430989*       | 2.157895        |
| SWARCHL(2,3)N(·)   | 184.0056        | 3.916024        | 8.440727        | 2.158818        |
| SWARCHL(2,3)t( . ) | 183.4115        | 3.865278        | 8.449593        | 2.157306        |
| SWARCHL(3,2)N(·)   | 179.1721        | 3.839258        | 8.586411        | 2.153293        |

Notes:

<!-- image -->

For  the  return  of the  US$,  the EG1RCH(l, l) performs  very well. For  the [LEJ2 and ILEI loss  functions, the  best  model is  the  Gaussian EG1RCH(l, l). When  the MAE is used  the GED EG1RCH(l, l) is  the best,  followed  closely  by  the  Gaussian SW ARCH(3, 2), which is the best when the MSE is used.

For  the return  on the  Cbond,  the G1RCH(l, 1)  using either  a Gaussian or Student-t specification performs best for the [LEJ2 and I LEI functions.  For the MAE or the MSE functions the Gaussian EG1RCH(l, l) is the best model.  It is worth mentioning that the Gaussian SW ARCH(3, 2) does  also well when we  used  the MSE, the MAE, and the I LEI functions.

## J oao Victor Issler

Table 13 Forecast Accuracy of  ARCH Models for the Return on the COCOA

|                  | Loss FUnction   | Loss FUnction   | Loss FUnction   | Loss FUnction   |
|------------------|-----------------|-----------------|-----------------|-----------------|
| Model            | M8E             | MAE             | [LEJ 2          | JLEJ            |
| OL8 Homocedastic | 60.29065        | 3.248362        | 12.25410        | 2.554517        |
| EGARCH(I,I)GED   | 58.96771        | 3.064281*       | 85.07656        | 4.501383        |
| EGARCH(I,I)N(.)  | 50.80501*       | 3.070752        | 9.683910*       | 2.307081*       |
| GARCH(I,I)N( . ) | 51.08158        | 3.087768        | 11.88679        | 2.457249        |
| TARCH(l,I)N(·)   | 58.61194        | 3.147152        | 11.17255        | 2.408486        |
| GARCH(I,I)t(·)   | 51.84851        | 3.291344        | 15.30956        | 2.698542        |
| 8WARCH(2,4)N(·)  | 52.84229        | 3.168131        | 17.49321        | 2.814531        |
| 8WARCH(2,2)t(-)  | 51.59023        | 3.170375        | 18.33362        | 2.833525        |

Notes:

<!-- image -->

For the return  on  COCOA, the Gaussian EG4RCH(l,l) per­ forms very well, with the smallest loss-function value when we used the M SE, the [LE]  2  , and the I LEI functions.  For the MAE function, the best model is also the EG4RCH(l, 1), when the Generalized Er­ ror Distribution is used.  In this case, the Gaussian EG4RCH(l, 1) gets  the second smallest statistic.  It is worth  mentioning that  the Gaussian G4RCH(l, 1) does also well when we used the [LE]2 and the I LEI functions.

For the return on Telebras, the Gaussian G4RCH(l, 1) performs best  for  the [LEj2 and I LEI functions.  For the MAE function, the Gaussian EG4RCH(l, 1) is the best model, but for the MSE func­ tion,  the Gaussian T ARC  H(l, 1) is the best model.

Table 14 Forecast Accuracy of ARCH Models for  the Return on the TELEBRAS

|                    | Loss Function   | Loss Function   | Loss Function   | Loss Function   |
|--------------------|-----------------|-----------------|-----------------|-----------------|
| Model              | MSE             | MAE             | [ LE 2  ]       | I LE I          |
| OLS Homocedastic   | 1595.468        | 12.26207        | 9.962296        | 2.302542        |
| EGARCH(l,l)GED     | 1412.165        | 10.31947        | 8.001585        | 1.985133        |
| EGARCH(l,l)NO      | 1360.067        | 9.924305*       | 7.512093        | 1.933137        |
| GARCH(1,l)NO       | 1503.709        | 10.99655        | 6.857071  *     | 1.893813*       |
| TARCH(l,l)NO       | 1347.081  *     | 10.03158        | 7.581257        | 1.938151        |
| GARCH(l,l)tO       | 1513.173        | 11.16956        | 6.916737        | 1.902861        |
| SWARCHL(2,4)N(·)   | 1387.448        | 10.27614        | 6.869221        | 1.898802        |
| SWARCHL(2,4)t(·)   | 1387.997        | 10.34076        | 6.912706        | 1.894535        |
| SWARCHL(3,2)N( . ) | 1367.935        | 10.09478        | 7.073707        | 1.910460        |

Notes:

<!-- image -->

Overall, the Gaussian EG4.RCH(l, 1) performed very well.  Sim­ ilar results are obtained by Pagan and Schwert (1990) and Engle and Ng (1991). Since for the EG4.RCH model the impact of squared er­ rors  on the conditional variance is exponential, it is thought to react too  much to  lagged  standardized  errors. This  may  be  bad  if large errors are infrequent, with the model over-predicting the variance in response to a sequence of small errors.  However,  if large  errors are common, this feature may not be bad, since it also matters how well the model forecast outliers.

The forecasting performance SW ARCH models was not encour­ aging compared to other models of the ARCH class.  Hamilton and Susmel criticize standard G4.RC  H models for overestimating the per-

sistence of volatility!O  Indeed, they write in p. 316 that  "Engle and Mustafa (1992) concluded on the basis of stock option prices that the volatility  consequences  of the 1987 crash disappeared  more rapidly than is suggested by the ...  [behavior of the Student-t TARCH(I, 1) model]. Lamoureux and Lastrapes (1993) presented related evidence based  on  earlier  data  that  standard G1RCH models  overforecast the persistence in volatility" .  If this is  true,  our  forecasting results show that  overforecasting actually helped ARCH models that ne­ glect  regime  switching. This may be related to the frequency  and size of outliers for  Brazilian data.  If outliers are rare, it is probably not  very  good  to have  a model which  frequently  overestimates  the volatility of regular standardized errors.  However,  if outliers are fre­ quent,  overforecasting will hurt the forecast  of mid-sized errors but probably benefit  the forecast  of outliers. Since  these make a large contribution to the average forecasting error, the net result may be favorable to models with this feature.  Despite this conjecture,  It is worth noting that for the return on  the US$, where there are clearly distinct  regimes,  the  Gaussian SW ARCH(3, 2) performed  well,  as expected.

Finally, we present goodness-of -fit statistics for most regressions in  Tables 15 through 18. For the return on the  US$  and on Tele­ bras,  the  best  model is  the  Student-t SW ARCH(2, 4), although for Telebras,  using the Schwarz  criterium,  one  would  have  chosen  the Student-t G4RCH(I, 1), because the former has too many parame­ ters. For the return on the  Cbond  the best model is the Student-t G4RCH(I, I), and  for  the  return  on the  COCOA  the  best  is  the GED EG1RCH(I, I). These results partially rehabilitate models in the SW ARCH class, although it deserves further investigation why their forecasting performance is  not  as good as their goodness-of -fit statistics.

## Estimating and Forecasting the Volatility of Brazilian Finance Series

Table 15 Goodness-of-Fit Measures for ARCH Estimates of the Return of the US$

| Model             | Max[Log LJ   | AlC      | BIC      |
|-------------------|--------------|----------|----------|
| OLS Homocedastic  | -157.6977    | 0.305482 | 0.310242 |
| GARCH(1,l)N(·)    | 872.31       | -1.6714  | -1.6524  |
| EGARCH(1,1)N(.)   | 876.79       | -1.6781  | -1.6543  |
| GARCH(1,1)t(·)    | 945.66       | -1.8107  | -1.7869  |
| EGARCH(1,1)GED    | 931.75       | -1.782   | -1.7530  |
| TARCH(1,1)N(·)    | 882.56       | -1.689   | -1.1665  |
| SWARCH(2,4)N(.)   | 904.39       | -1.7236  | -1.6807  |
| SWARCH(2,4)t( . ) | 968.72*      | -1.8455* | -1.7979* |
| SWARCH(3,2)N(·)   | 909.67       | -1.7318  | -1.6842  |

Note:

(l)*Denotes the best model.

Table 16 Goodness-of-Fit Measures for  ARCH Estimates of the Return on the CBOND

| Model            | Max[Log LJ   | AlC      | BIC      |
|------------------|--------------|----------|----------|
| OL8 Homocedastic | -2239.394    | 4.095785 | 4.100353 |
| GARCH(1,1)N(·)   | -2001.36     | 3.6661   | 3.6844   |
| EGARCH(1,1)N(. ) | -1981.85     | 3.6323   | 3.6551   |
| GARCH(1,1)t(·)   | -1928.77*    | 3.5352*  | 3.5439*  |
| EGARCH(1,1)GED   | -1937.33     | 3.553    | 3.580    |
| TARCH(1,1)N(-)   | -1980.54     | 3.630    | 3.653    |
| 8WARCH(2,3)N(·)  | -1944.22     | 3.5708   | 3.6119   |
| 8WARCH(2,3)t(·)  | -1943.26     | 3.5709   | 3.6165   |
| 8WARCH(3,2)N(. ) | -1946.38     | 3.5766   | 3.6222   |

Note:

(1  )*Denotes the best model.

## J oao Victor IssIer

## Goodness-of-Fit Measures for ARCH Estimates of the Return on COCOA

| Model            | Max[Lag LJ   | AlC      | BIC      |
|------------------|--------------|----------|----------|
| OLS Homocedastic | -4219.340    | 3.819312 | 3.821891 |
| GARCH(1,l)N(. )  | -4078.65     | 3.6947   | 3.7050   |
| EGARCH(l,l)N(-)  | -4090.70     | 3.7065   | 3.7194   |
| GARCH(l,l)t(-)   | -3910.23     | 3.5432   | 3.5561   |
| EGARCH(l,l)GED   | -3889.42*    | 3.5190'  | 3.5340*  |
| TARCH(l,l)N(-)   | -4077.27     | 3.694    | 3.707    |
| SWARCH(2,4)N(·)  | -3968.02     | 3.6000   | 3.6258   |
| SWARCH(2,2)t(-)  | -3912.25     | 3.5468   | 3.5649   |

Note:

Table 18 Goodness-af-Fit Measures far ARCH Estimates of the Return on TELEBRAS

| Model            | Max[Lag LJ   | AlC      | BIC      |
|------------------|--------------|----------|----------|
| OLS Homocedastic | -2691.018    | 5.181940 | 5.186701 |
| GARCH(l,l)N(·)   | -2498.84     | 4.8178   | 4.8368   |
| EGARCH(l,l)NO    | -2483.38     | 4.7899   | 4.8137   |
| GARCH(l,l)t(·)   | -2485.67     | 4.7944   | 4.8034*  |
| EGARCH(l,l)GED   | -2488.63     | 4.802    | 4.831    |
| TARCH(l,l)N(·)   | -2483.45     | 4.7901   | 4.8139   |
| SWARCH(2,4)N(·)  | -2500.07     | 4.8298   | 4.8726   |
| SWARCH(2,4)t(. ) | -2475.90'    | 4.7852*  | 4.8328   |
| SWARCH(3,2)N(-)  | -2482.63     | 4.7981   | 4.8457   |

Note:

(1 )*Denotes the best model.

Estimating and Forecasting the Volatility of Brazilian Finance Series

## 5.  Conclusions  and  Further  Research

The goal of this paper was to present a comprehensive  empiri­ cal analysis of the return and  conditional variance of four Brazilian financial series using models of the ARCH class.  To discuss the em­ pirical results  in greater depth,  a self-contained  theoretical Section presents ARCH models in  a way  that  it  is  useful  for  the  applied researcher.  References to complete surveys are also given.

The empirical results show a distinct behavior for  these four fi­ nancial series.  Although all series share ARCH and are leptokurtic relative  to  the  Normal,  the  return  on the  US$  has  clearly  regime switching  and  no  asymmetry for  the  variance,  the  return  on  CO­ COA has no asymmetry, while the returns on the Cbond and Tele­ bras have clear signs of asymmetry favoring the leverage effect.  All these stylized  facts  were modelled using the ARCH class. Regard­ ing forecasting, the best model overall was the EGARCH(l, 1), in its Gaussian version. Different  versions  of the GARCH(l,l) also  per­ formed well, while the SW ARCH only did well for the return on the US$, which has a distinct pattern of regimes for the sample period. Regarding goodness-of-fit statistics,  the SW ARCH model did well, followed closely by the Student-t GARCH(l, 1).

Understanding forecasting results deserves further investigation. Maybe  a  comparison  between  models  of  the EGARCH and  the SW ARCH family  would  be useful,  since  it  may  shed  light  in why the former does so  well and the latter does not.  This is  particulm·ly intriguing in light of our goodness-of-fit results.

Submitted  on March 1999 and revised on May 1 999.

## References

Akaike,  H.  1973. "Information  theory  and  an  extension  of the maximum likelihood principle" . In:  Petrov,  B.N. &amp; Csaki,  F. ( eds. ) . Second International Symposium  on Information  The­ ory. Akademiai Kiad6: Budapest.

- Black,  F.  1976. "Studies  of stock price  volatility  changes". P ro­ ceedings  from the American Statistical Association, Business and Economic Statistics Section, 177-18l.
- \_\_\_\_ &amp; Scholes, M. 1973.  "The pricing of options and corpo­ rate liabilities" . Journal of Political Economy, 81:637-659.

Bollerslev, Tim.  1986.  "Generalized autoregressive conditional het­ eroskedasticity" . Journal of Econometrics, 31:307-327.

- \_\_\_\_ . 1987.  "A conditional heteroskedastic time series model for speculative prices and rates of return" . Review of  Economics and Statistics, 69:542-547.
- \_\_\_\_ ; Chou, Ray Y. &amp; Kroner, Kenneth F. 1992.  "ARCH mod­ eling in finance: a review of the theory and empirical evidence" . Journal of Econometrics, 52:559.
- \_\_\_\_ &amp; Wooldridge, Jeffrey M. 1992.  " Q uasi-maximum like­ lihood  estimation  and  inference  in  dynamic  models  with  time varying covariances". Econometric Reviews, 11:143-172.
- \_\_\_\_ ; Engle,  Robert  F. &amp; Nelson, Daniel B.  1994. "ARCH models". Handbook  of  Econometrics, 4:chapter  49,  North­ Holland.
- Box,  G.E.P. &amp; Jenkins, G.M. 1976.  "Time series analysis: forecast­ ing and  control" .  2  ed.  Holden day:  San Francisco.
- Campbell, J.Y.;  Lo,  A.W. &amp; MacKinlay,  A.C.  1997. "The econo­ metrics of financial  markets" .  Princeton: Princeton University Press.

Estimating and Forecasting the Volatility of Brazilian Finance Series

Diebold, Francis X. 1986.  "Modeling the persistence of conditional variances:  a comment" . Econometric Reviews, 5:51-56.

Engle,  Robert F.  1982. "Autoregressive conditional heteroskedas­ ticity  with  estimates  of the  variance  of UK  inflation" . Econo­ metrica, 50:987-1008.

- \_\_\_\_ . 1983.  "Estimates of the variance of US inflation based upon the ARCH model" . Journal of Money, Credit and Banking, 15.
- \_\_\_\_ . 1995. "ARCH:  selected  readings" . Oxford:  Oxford University Press.
- \_\_\_\_ &amp;  Gonzalez-Rivera,  G.  1991. "Semiparametric  ARCH models" . Journal of Business  and Economic Statistics, 9:345359.
- \_\_\_\_ &amp; Mustafa,  C.  1992. "Implied ARCH models from op­ tions prices" . Journal of Econometrics, 52:289-311.
- \_\_\_\_ &amp; Ng, Victor K. 1993.  "Measuring and testing the impact of news on volatility" . Journal of Finance, 48:1022-1082.

Friedman, M.  1977.  "Nobel lecture:  inflation and  unemployment" . Journal of Political Economy, 85.

Gallant,  A.R. &amp;  Tauchen,  G. 1989.  "Semi non-parametric estima­ tion of conditionally constrained heterogeneous processes: asset pricing applications". Econometrica, 57:1091-1120.

- \_\_\_\_ ;  Hsieh,  D.A. &amp; Tauchen, G.  1991.  "On fitting a recalci­ trant series: the pound / dollar exchange rate 1974-83" .  In:  Bar­ nett, W.A.; Powell, J. &amp; Tauchen, G. ( eds. ) . Nonpammetric and Semipammetric Methods  in Econometrics  and Statistics. Cam­ bridge University Press: Cambridge.

- \_\_\_\_ ; , Rossi,  P.E.  &amp;  Tauchen,  G.  1992. "Stock  prices  and volume". Review of Financial Studies, 5:199-242.
- \_\_\_\_ ;  Rossi,  P.E. &amp;  Tauchen,  G.  1993.  "Non-linear dynamic structures" . Econometrica, 61 :871-907.

Glosten,  L.R.; Jagannathan, R. &amp; Runkle, D.  1993.  "On the rela­ tion between the expected value and the volatility of the normal excess  return  on stocks" . Journal of Finance, 48:1779-180l.

Granger, C.W.J. &amp; Andersen, A. 1978.  "An introduction to bilinear time-series models" .  G6ttingen.

- Hamilton, James D. 1994.  "Time series analysis" .  Princeton Uni­ versity Press.
- \_\_\_\_ &amp; Susmel, Raul.  1994.  "Autoregressive conditional het­ eroskedasticity  and  changes  in regime" . Journal of Economet­ rics, 64:307-333.
- Jm'que,  C.  &amp;  Bera,  A.  1987. "A  test  for  normality  of observa­ tions and regression residuals" . International Statistical Review, 55:  163-172.

Lamoureux,  Christopher  G. &amp;  Lastrapes,  William D.  1990. "Per­ sistence in variance, structural change and the GARCH model" . Journal of Business and Economic Statistics, 8:225-234.

- \_\_\_\_ &amp; Lastrapes, William D. 1993.  "Forecasting stock return variance: toward an understanding of stochastic implied volatil­ ities" . Review of Financial Studies, 5:293-326.

Mandelbrot, B. 1963.  "The variation of certain speculative prices" . Journal of Business, 36:394-419.

Nelson,  D.B.  1990. "ARCH models as  diffusion approximations". Journal of Econometrics, 45:7-38.

- \_\_\_\_ .  1991.  "Conditional heteroskedasticity in asset returns: a new approach". Econometrica, 59:347-370.

Estimating and Forecasting the Volatility of Brazilian Finance Series

Newey,  Whitney  &amp;  West,  Kenneth. 1987. "A  simple  positive semi-definite,  heteroskedasticity  and  autocorrelation  consistent covariance matrix". Econometrica, 55:703-708.

Okun, A. 1971.  "The mirage of steady inflation" . Brookings Papers on Economic Activity, 2.

Pagan, A.R. &amp; Schwert, G.W. 1990.  "Alternative models for condi­ tional stock volatility". Journal of Econometrics, 45:267-290.

Perron, Pierre.  1989.  "The great crash, the oil price shock, and the unit-root hypothesis" . Econometrica, 51:1361-1401.

Schwarz,  G. 1978.  "Estimating the dimension of a model" . Annals of Statistics, 6:461-464.

Tauchen,  George. 1986. "Statistical  properties  of  generalized method-of-moments  estimators  of  structural  parameters  ob­ tained from financial market data" . Journal of Business 1'3 Eco­ nomic Statistics, 4:397-416.

Weiss,  A.A. 1986.  "Asymptotic theory for  ARCH models: estima­ tion and testing" . Econometric  Theory, 2:107-131.

Zakoian,  J.M.  1990. "Threshold  heteroskedastic  models" . Manu­ script,  CREST, INSEE, Paris.