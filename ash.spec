Summary:	Small bourne shell from Berkeley
Summary(de):	Kleine Bourne-Shell von Berkeley
Summary(fr):	Shell Bourne réduit de Berkeley
Summary(pl):	Ma³y shell bourne'a 
Summary(tr):	Ufak bir bourne kabuðu
Name:		ash
Version:	0.2
Release:	24
License:	BSD
Group:		Shells
Group(pl):	Pow³oki
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/shells/%{name}-linux-%{version}.tar.gz
Patch0:		%{name}-make.patch
Patch1:		%{name}-mknodes.patch
Patch2:		ash-fd.patch
Patch3:		ash-exit.patch
Patch4:		ash-echo.patch
Patch5:		ash-mksyntax.patch
Patch6:		ash-linux-sighup.patch
Patch7:		ash-linux-mkinit.patch
Prereq:		fileutils
Prereq:		grep
BuildRequires:	glibc-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	mkinitrd <= 1.7

%define		_prefix		/

%description
ash is a bourne shell clone from Berkeley. It supports all of the
standard Bourne shell commands and has the advantage of supporting
them while remaining considerably smaller than bash.

%description -l de
ash ist ein Bourne-Shell-Clone aus Berkeley, der alle
Standard-Bourne-Shell- Befehle unterstützt und dennoch erheblich
weniger Platz beansprucht als bash.

%description -l fr
ash est un clone Berkeley du shell Bourne. Il gère toutes les
commandes standard du shell Bourne et a l'avantage de les gérer tout
en restant considérablement plus petit que bash.

%description -l pl
Ash jest klonem shell'a Bourne'a z Berkeley. Obs³uguje standardowe
komendy shell'a Bourne'a i jest mniejszy ni¿ bash.

%description -l tr
ash, Berkeley'in bir bourne kabuðu kopyasýdýr. Standart bourne kabuðu
komutlarýnýn tümünü destekler ve bash kabuðundan daha küçük olma
avantajýna sahiptir.

%package static
Summary:	Small bourne shell from Berkeley
Summary(de):	Kleine Bourne-Shell von Berkeley
Summary(fr):	Shell Bourne réduit de Berkeley
Summary(pl):	Ma³y shell bourne'a 
Summary(tr):	Ufak bir bourne kabuðu
Group:		Shells
Group(pl):	Pow³oki
Prereq:		fileutils
Prereq:		grep
Conflicts:	mkinitrd <= 1.7

%description static
ash is a bourne shell clone from Berkeley. It supports all of the
standard Bourne shell commands and has the advantage of supporting
them while remaining considerably smaller than bash.

%description static -l de
ash ist ein Bourne-Shell-Clone aus Berkeley, der alle
Standard-Bourne-Shell- Befehle unterstützt und dennoch erheblich
weniger Platz beansprucht als bash.

%description static -l fr
ash est un clone Berkeley du shell Bourne. Il gère toutes les
commandes standard du shell Bourne et a l'avantage de les gérer tout
en restant considérablement plus petit que bash.

%description static -l pl
Ash jest klonem shell'a Bourne'a z Berkeley. Obs³uguje standardowe
komendy shell'a Bourne'a i jest mniejszy ni¿ bash.

%description static -l tr
ash, Berkeley'in bir bourne kabuðu kopyasýdýr. Standart bourne kabuðu
komutlarýnýn tümünü destekler ve bash kabuðundan daha küçük olma
avantajýna sahiptir.

%prep
%setup -q -n ash-linux-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
%{__make} OPT_FLAGS="$RPM_OPT_FLAGS" STATIC=-static
mv -f sh ash.static
%{__make} OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1}

install sh $RPM_BUILD_ROOT%{_bindir}/ash
install ash.static $RPM_BUILD_ROOT%{_bindir}/ash.static
install sh.1 $RPM_BUILD_ROOT%{_mandir}/man1/ash.1
echo ".so ash.1" > $RPM_BUILD_ROOT%{_mandir}/man1/bsh.1
ln -sf ash $RPM_BUILD_ROOT/%{_bindir}/bsh

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%post
if [ ! -f /etc/shells ]; then
        echo "%{_bindir}/ash" > /etc/shells
        echo "%{_bindir}/bsh" >> /etc/shells
else
        if ! grep '^%{_bindir}/ash$' /etc/shells > /dev/null; then
                echo "%{_bindir}/ash" >> /etc/shells
        fi
        if ! grep '^%{_bindir}/bsh$' /etc/shells > /dev/null; then
                echo "%{_bindir}/bsh" >> /etc/shells
        fi
fi

%post static
if [ ! -f /etc/shells ]; then
        echo "%{_bindir}/ash.static" >> /etc/shells
else
        if ! grep '^%{_bindir}/ash.static$' /etc/shells > /dev/null; then
                echo "%{_bindir}/ash.static" >> /etc/shells
        fi
fi

%preun
if [ "$0" = 0 ]; then
        grep -v %{_bindir}/ash /etc/shells | grep -v %{_bindir}/bsh | grep -v %{_bindir}/ash.static > /etc/shells.new
        mv -f /etc/shells.new /etc/shells
fi

%preun static
if [ "$0" = 0 ]; then
        grep -v %{_bindir}/ash /etc/shells | grep -v %{_bindir}/bsh > /etc/shells.new
        mv -f /etc/shells.new /etc/shells
fi

%verifyscript
for n in ash bsh ash.static; do
    echo -n "Looking for $n in /etc/shells... "
    if ! grep "^%{_bindir}/${n}\$" /etc/shells > /dev/null; then
	echo "missing"
	echo "${n} missing from /etc/shells" >&2
    else
	echo "found"
    fi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ash
%attr(755,root,root) %{_bindir}/bsh
%{_mandir}/man1/*

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ash.static
