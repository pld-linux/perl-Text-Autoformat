# $Revision: 1.3 $
%define	pdir	Text
%define	pnam	Autoformat
%include	/usr/lib/rpm/macros.perl
Summary:	Text-Autoformat perl module
Summary(pl):	Modu³ perla Text-Autoformat
Name:		perl-Text-Autoformat
Version:	1.04
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(da):	Udvikling/Sprog/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(is):	Þróunartól/Forritunarmál/Perl
Group(it):	Sviluppo/Linguaggi/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(no):	Utvikling/Programmeringsspråk/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Group(sl):	Razvoj/Jeziki/Perl
Group(sv):	Utveckling/Språk/Perl
Group(uk):	òÏÚÒÏÂËÁ/íÏ×É/Perl
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
Text::Autoformat udostêpnia inteligentne formatowanie czystego tekstu
bez potrzeby jamkichkolwiek znaczników. Modu³ rozpoznaje internetowe
konwencje cytowania, szeroki zasób wyliczeñ i wiele schematów, tekst
centrowany, cytaty blokowe - i ka¿dy z nich odpowiednio reformatuje.
Inne opcje pozwalaj± u¿ytkownikowi regulowaæ odstêpy miêdzy s³owami
i miêdzy akapitami, justowaæ tekst i stosowaæ ró¿ne schematy wielko¶ci
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
