Summary:	PD Curses for DJGPP
Summary(pl):	PD Curses dla DJGPP
Name:		crossdjgpp-pdcurses
Version:	24
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Source0:	ftp://ftp.delorie.com/djgpp/v2misc/pdcur%{version}s.zip
BuildRequires:	crossdjgpp-gcc
Requires:	crossdjgpp-gcc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define target i386-pc-msdosdjgpp

%description
PD Curses for DJGPP.

%description -l pl
PD Curses dla DJGPP.

%prep
%setup -c -T -q -n contrib/pdcur%{version}
cd ../..
unzip -a %{SOURCE0} > /dev/null

%build
mkdir obj
cp -f dos/gccdos.* obj/
cd obj
ln -sf gccdos.mak Makefile
%{__make} CC=%{target}-gcc DJDIR=$PWD/../../.. libpdcurses.a libpanel.a

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/%{target}/{lib,include}

install curses.h curspriv.h panel.h $RPM_BUILD_ROOT%{_prefix}/%{target}/include
install obj/libpdcurses.a obj/libpanel.a $RPM_BUILD_ROOT%{_prefix}/%{target}/lib
# convinience link
ln -sf libpdcurses.a $RPM_BUILD_ROOT%{_prefix}/%{target}/lib/libcurses.a

mv -f maintain.er MAINTAINER
gzip -9nf README MAINTAINER TODO readme.*

# .man suffix is misleading...
for f in intro latin-1 overview x11 ; do
	gzip < doc/$f.man > $f.txt.gz
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_prefix}/%{target}/lib/*
%{_prefix}/%{target}/include/*
