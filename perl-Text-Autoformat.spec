# $Revision: 1.3 $
%define	pdir	Text
%define	pnam	Autoformat
%include	/usr/lib/rpm/macros.perl
Summary:	Text-Autoformat perl module
Summary(pl):	Modu� perla Text-Autoformat
Name:		perl-Text-Autoformat
Version:	1.04
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(da):	Udvikling/Sprog/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(is):	�r�unart�l/Forritunarm�l/Perl
Group(it):	Sviluppo/Linguaggi/Perl
Group(ja):	��ȯ/����/Perl
Group(no):	Utvikling/Programmeringsspr�k/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Group(sl):	Razvoj/Jeziki/Perl
Group(sv):	Utveckling/Spr�k/Perl
Group(uk):	��������/����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
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
bez potrzeby jamkichkolwiek znacznik�w. Modu� rozpoznaje internetowe
konwencje cytowania, szeroki zas�b wylicze� i wiele schemat�w, tekst
centrowany, cytaty blokowe - i ka�dy z nich odpowiednio reformatuje.
Inne opcje pozwalaj� u�ytkownikowi regulowa� odst�py mi�dzy s�owami
i mi�dzy akapitami, justowa� tekst i stosowa� r�ne schematy wielko�ci
liter.

%prep
%setup -q -n Text-Autoformat-%{version}

%build
perl Makefile.PL
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%doc demo.pl
%{perl_sitelib}/Text/Autoformat.pm
%{_mandir}/man3/*
