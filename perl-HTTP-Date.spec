#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	HTTP
%define		pnam	Date
Summary:	HTTP::Date - date conversion routines
Summary(pl.UTF-8):	HTTP::Date - funkcje do konwersji dat
Name:		perl-HTTP-Date
Version:	6.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTTP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	60462359bfeb1e6d14602508cfd07885
URL:		https://metacpan.org/release/HTTP-Date
%if %{with tests}
BuildRequires:	perl(Time::Local) >= 1.28
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	perl-devel >= 1:5.8.8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Conflicts:	perl-libwww < 6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides functions that deal the date formats used by the
HTTP protocol (and then some more).  Only the first two functions,
time2str() and str2time(), are exported by default.

%description -l pl.UTF-8
Ten moduł udostępnia funkcje obsługujące formaty danych używane w
protokole HTTP (i paru innych). Domyślnie eksportowane są tylko dwie
funkcje: time2str() i str2time().

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/HTTP/Date.pm
%{_mandir}/man3/HTTP::Date.3pm*
