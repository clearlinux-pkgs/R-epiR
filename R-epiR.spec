#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-epiR
Version  : 2.0.26
Release  : 37
URL      : https://cran.r-project.org/src/contrib/epiR_2.0.26.tar.gz
Source0  : https://cran.r-project.org/src/contrib/epiR_2.0.26.tar.gz
Summary  : Tools for the Analysis of Epidemiological Data
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-BiasedUrn
Requires: R-ggplot2
Requires: R-lubridate
Requires: R-mapproj
Requires: R-maptools
Requires: R-pander
Requires: R-plyr
Requires: R-rgdal
Requires: R-rgeos
Requires: R-spData
Requires: R-spatstat
BuildRequires : R-BiasedUrn
BuildRequires : R-ggplot2
BuildRequires : R-lubridate
BuildRequires : R-mapproj
BuildRequires : R-maptools
BuildRequires : R-pander
BuildRequires : R-plyr
BuildRequires : R-rgdal
BuildRequires : R-rgeos
BuildRequires : R-spData
BuildRequires : R-spatstat
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n epiR
cd %{_builddir}/epiR

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622561110

%install
export SOURCE_DATE_EPOCH=1622561110
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library epiR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library epiR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library epiR
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc epiR || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/epiR/DESCRIPTION
/usr/lib64/R/library/epiR/INDEX
/usr/lib64/R/library/epiR/Meta/Rd.rds
/usr/lib64/R/library/epiR/Meta/data.rds
/usr/lib64/R/library/epiR/Meta/features.rds
/usr/lib64/R/library/epiR/Meta/hsearch.rds
/usr/lib64/R/library/epiR/Meta/links.rds
/usr/lib64/R/library/epiR/Meta/nsInfo.rds
/usr/lib64/R/library/epiR/Meta/package.rds
/usr/lib64/R/library/epiR/Meta/vignette.rds
/usr/lib64/R/library/epiR/NAMESPACE
/usr/lib64/R/library/epiR/NEWS
/usr/lib64/R/library/epiR/R/epiR
/usr/lib64/R/library/epiR/R/epiR.rdb
/usr/lib64/R/library/epiR/R/epiR.rdx
/usr/lib64/R/library/epiR/data/epi.SClip.RData
/usr/lib64/R/library/epiR/data/epi.epidural.RData
/usr/lib64/R/library/epiR/data/epi.incin.RData
/usr/lib64/R/library/epiR/doc/epiR_RSurveillance.R
/usr/lib64/R/library/epiR/doc/epiR_RSurveillance.Rmd
/usr/lib64/R/library/epiR/doc/epiR_RSurveillance.html
/usr/lib64/R/library/epiR/doc/epiR_descriptive.R
/usr/lib64/R/library/epiR/doc/epiR_descriptive.Rmd
/usr/lib64/R/library/epiR/doc/epiR_descriptive.html
/usr/lib64/R/library/epiR/doc/epiR_sample_size.R
/usr/lib64/R/library/epiR/doc/epiR_sample_size.Rmd
/usr/lib64/R/library/epiR/doc/epiR_sample_size.html
/usr/lib64/R/library/epiR/doc/epiR_surveillance.R
/usr/lib64/R/library/epiR/doc/epiR_surveillance.Rmd
/usr/lib64/R/library/epiR/doc/epiR_surveillance.html
/usr/lib64/R/library/epiR/doc/index.html
/usr/lib64/R/library/epiR/help/AnIndex
/usr/lib64/R/library/epiR/help/aliases.rds
/usr/lib64/R/library/epiR/help/epiR.rdb
/usr/lib64/R/library/epiR/help/epiR.rdx
/usr/lib64/R/library/epiR/help/paths.rds
/usr/lib64/R/library/epiR/html/00Index.html
/usr/lib64/R/library/epiR/html/R.css
