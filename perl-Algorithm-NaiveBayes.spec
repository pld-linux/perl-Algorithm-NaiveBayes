#
# Conditional build:
%bcond_without	tests	# don't perform "make test"

%define		pdir	Algorithm
%define		pnam	NaiveBayes
Summary:	Algorithm::NaiveBayes - Bayesian prediction of categories
Summary(pl.UTF-8):	Algorithm::NaiveBayes - bayesowskie przewidywanie kategorii
Name:		perl-Algorithm-NaiveBayes
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bd461c9ea2f140a75d5364cc98c2ef09
URL:		http://search.cpan.org/dist/Algorithm-NaiveBayes/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements the classic "Naive Bayes" machine learning
algorithm. It is a well-studied probabilistic algorithm often used in
automatic text categorization. Compared to other algorithms (kNN, SVM,
Decision Trees), it's pretty fast and reasonably competitive in the
quality of its results.

%description -l pl.UTF-8
Ten moduł jest implementacją klasycznego "naiwnego bayesowskiego"
algorytmu uczenia maszyny. Jest to dobrze przestudiowany algorytm
probabilistyczny często używany przy automatycznej kategoryzacji
tekstu. W porównaniu do innych algorytmów (kNN, SVM, drzewa decyzyjne)
jest dość szybki i w miarę konkurencyjny jeśli chodzi o jakość
wyników.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change*
%{perl_vendorlib}/Algorithm/*.pm
%{perl_vendorlib}/Algorithm/NaiveBayes
%{_mandir}/man3/*
