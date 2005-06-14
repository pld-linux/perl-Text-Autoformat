#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	Autoformat
Summary:	Text::Autoformat perl module
Summary(pl):	Modu� perla Text::Autoformat
Name:		perl-Text-Autoformat
Version:	1.13
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1a944e3e21e176178bb4f87a6068f041
BuildRequires:	perl-Text-Reform >= 1.11
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Text-Reform >= 1.11
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Autoformat provides intelligent formatting of plaintext without
the need for any kind of embedded mark-up. The module recognizes
Internet quoting conventions, a wide range of bulleting and number
schemes, centred text, and block quotations, and reformats each
appropriately. Other options allow the user to adjust inter-word and
inter-paragraph spacing, justify text, and impose various
capitalization schemes.

%description -l pl
Text::Autoformat udost�pnia inteligentne formatowanie czystego tekstu
bez potrzeby jakichkolwiek znacznik�w. Modu� rozpoznaje internetowe
konwencje cytowania, szeroki zas�b wylicze� i wiele schemat�w, tekst
centrowany, cytaty blokowe - i ka�dy z nich odpowiednio reformatuje.
Inne opcje pozwalaj� u�ytkownikowi regulowa� odst�py mi�dzy s�owami
i mi�dzy akapitami, justowa� tekst i stosowa� r�ne schematy wielko�ci
liter.

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
%doc Changes
%{perl_vendorlib}/Text/Autoformat.pm
%{_mandir}/man3/*
