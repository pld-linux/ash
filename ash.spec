Summary:	Small bourne shell from Berkeley
Summary(de):	Kleine Bourne-Shell von Berkeley
Summary(fr):	Shell Bourne réduit de Berkeley
Summary(pl):	Ma³y shell bourne'a 
Summary(tr):	Ufak bir bourne kabuðu
Name:		ash
Version:	0.3.1
Release:	1
License:	BSD
Group:		Applications/Shells
Group(de):	Applikationen/Shells
Group(pl):	Aplikacje/Pow³oki
Source0:	ftp://ftp.pld.org.pl/people/malekith/%{name}-linux-%{version}.tar.gz
Prereq:		fileutils
Prereq:		grep
BuildRequires:	glibc-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	mkinitrd <= 1.7

%define		_bindir		/bin

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
Group:		Applications/Shells
Group(de):	Applikationen/Shells
Group(pl):	Aplikacje/Pow³oki
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

%build
%{__make} OPT_FLAGS="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS}" \
	LDFLAGS="-static %{!?debug:-s}"
mv -f sh ash.static
%{__make} OPT_FLAGS="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS}" \
	LDFLAGS="%{!?debug:-s}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1}

install sh $RPM_BUILD_ROOT%{_bindir}/ash
install ash.static $RPM_BUILD_ROOT%{_bindir}/ash.static
install sh.1 $RPM_BUILD_ROOT%{_mandir}/man1/ash.1
echo ".so ash.1" > $RPM_BUILD_ROOT%{_mandir}/man1/bsh.1
ln -sf ash $RPM_BUILD_ROOT/%{_bindir}/bsh

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
