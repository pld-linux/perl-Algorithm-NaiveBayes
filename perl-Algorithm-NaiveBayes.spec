#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Algorithm
%define	pnam	NaiveBayes
Summary:	Algorithm::NaiveBayes - Bayesian prediction of categories
Summary(pl):	Algorithm::NaiveBayes - bayesowskie przewidywanie kategorii
Name:		perl-Algorithm-NaiveBayes
Version:	0.01
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements the classic "Naive Bayes" machine learning
algorithm. It is a well-studied probabilistic algorithm often used in
automatic text categorization. Compared to other algorithms (kNN, SVM,
Decision Trees), it's pretty fast and reasonably competitive in the
quality of its results.

#%%description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change*
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
