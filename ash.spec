Summary:     	Small bourne shell from Berkeley
Summary(de): 	Kleine Bourne-Shell von Berkeley
Summary(fr): 	Shell Bourne réduit de Berkeley
Summary(pl):	Ma³y shell bourne'a 
Summary(tr):	Ufak bir bourne kabuðu
Name:        	ash
Version:     	0.2
Release:     	18
Copyright:   	BSD
Group:       	Shells
Group(pl):	Pow³oki
Source:      	ftp://sunsite.unc.edu/pub/Linux/system/shells/ash-linux-%{version}.tar.gz
Patch0:       	ash-make.patch
Patch1:		ash-mknodes.patch
Prereq:      	fileutils
Prereq:		grep
BuildRoot:	/tmp/%{name}-%{version}-root
Conflicts:   	mkinitrd <= 1.7

%description
ash is a bourne shell clone from Berkeley.  It supports all of the standard
Bourne shell commands and has the advantage of supporting them while 
remaining considerably smaller than bash. 

%description -l de
ash ist ein Bourne-Shell-Clone aus Berkeley, der alle Standard-Bourne-Shell-
Befehle unterstützt und dennoch erheblich weniger Platz beansprucht als bash. 

%description -l fr
ash est un clone Berkeley du shell Bourne. Il gère toutes les commandes
standard du shell Bourne et a l'avantage de les gérer tout en restant
considérablement plus petit que bash.

%description -l pl
Ash jest klonem shell'a Bourne'a z Berkely. Obs³uguje standardowe komendy
shell'a Bourne'a i jest mniejszy ni¿ bash. 

%description -l tr
ash, Berkeley'in bir bourne kabuðu kopyasýdýr. Standart bourne kabuðu
komutlarýnýn tümünü destekler ve bash kabuðundan daha küçük olma
avantajýna sahiptir.

%package static
Summary:     	Small bourne shell from Berkeley
Summary(de): 	Kleine Bourne-Shell von Berkeley
Summary(fr): 	Shell Bourne réduit de Berkeley
Summary(pl):	Ma³y shell bourne'a 
Summary(tr):	Ufak bir bourne kabuðu
Group:       	Shells
Group(pl):	Pow³oki
Prereq:      	fileutils
Prereq:		grep
Conflicts:   	mkinitrd <= 1.7

%description static
ash is a bourne shell clone from Berkeley.  It supports all of the standard
Bourne shell commands and has the advantage of supporting them while 
remaining considerably smaller than bash. 

%description static -l de
ash ist ein Bourne-Shell-Clone aus Berkeley, der alle Standard-Bourne-Shell-
Befehle unterstützt und dennoch erheblich weniger Platz beansprucht als bash. 

%description static -l fr
ash est un clone Berkeley du shell Bourne. Il gère toutes les commandes
standard du shell Bourne et a l'avantage de les gérer tout en restant
considérablement plus petit que bash.

%description static -l pl
Ash jest klonem shell'a Bourne'a z Berkely. Obs³uguje standardowe komendy
shell'a Bourne'a i jest mniejszy ni¿ bash. 

%description static -l tr
ash, Berkeley'in bir bourne kabuðu kopyasýdýr. Standart bourne kabuðu
komutlarýnýn tümünü destekler ve bash kabuðundan daha küçük olma
avantajýna sahiptir.

%prep
%setup  -q -n ash-linux-%{version}
%patch0 -p1
%patch1 -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{bin,%{_mandir}/man1}

install sh $RPM_BUILD_ROOT/bin/ash
install sh.1 $RPM_BUILD_ROOT%{_mandir}/man1/ash.1
echo ".so ash.1" > $RPM_BUILD_ROOT%{_mandir}/man1/bsh.1
ln -sf ash $RPM_BUILD_ROOT/bin/bsh

rm -f sh
make STATIC=-static

install sh $RPM_BUILD_ROOT/bin/ash.static

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%post
if [ ! -f /etc/shells ]; then
        echo "/bin/ash" > /etc/shells
        echo "/bin/bsh" >> /etc/shells
else
        if ! grep '^/bin/ash$' /etc/shells > /dev/null; then
                echo "/bin/ash" >> /etc/shells
        fi
        if ! grep '^/bin/bsh$' /etc/shells > /dev/null; then
                echo "/bin/bsh" >> /etc/shells
        fi
fi

%post static
if [ ! -f /etc/shells ]; then
        echo "/bin/ash.static" >> /etc/shells
else
        if ! grep '^/bin/ash.static$' /etc/shells > /dev/null; then
                echo "/bin/ash.static" >> /etc/shells
        fi
fi


%preun
if [ "$0" = 0 ]; then
        grep -v /bin/ash /etc/shells | grep -v /bin/bsh | grep -v /bin/ash.static > /etc/shells.new
        mv /etc/shells.new /etc/shells
fi

%preun static
if [ "$0" = 0 ]; then
        grep -v /bin/ash /etc/shells | grep -v /bin/bsh > /etc/shells.new
        mv /etc/shells.new /etc/shells
fi


%verifyscript
for n in ash bsh ash.static; do
    echo -n "Looking for $n in /etc/shells... "
    if ! grep "^/bin/${n}\$" /etc/shells > /dev/null; then
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
%attr(755,root,root) /bin/ash
/bin/bsh
%{_mandir}/man1/*

%files static
%defattr(644,root,root,755)
%attr(755,root,root) /bin/ash.static
